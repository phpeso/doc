Proxies and Dummy Services
##########################

.. highlight:: php

Proxies and Dummy Services are defined in the core library, ``peso/core``.

ChainService
============

``\Peso\Core\Services\ChainService($service1, $service2, ...)``

Chain service allows you to request data from several sources::

    <?php

    use Peso\Core\Services\ChainService;
    use Peso\Peso\CurrencyConverter;
    use Peso\Services\CzechNationalBankService;
    use Peso\Services\EuropeanCentralBankService;

    $converter = new CurrencyConverter(new ChainService(
        new EuropeanCentralBankService(),
        new CzechNationalBankService(),
    ));

    // ECB doesn't know that
    echo $converter->convertOnDate('1.20', 'USD', 'CZK', 2, '2025-06-13'); // 25.88

TrivialService
==============

.. versionadded:: 1.2

TrivialService returns rate of 1 when currency is exchanged to itself.
Use it when the service does not contain a self-reference entry for the currency
or to prefix a service with limits to avoid pointless calls::

    <?php

    use Peso\Core\Services\TrivialService;
    use Peso\Peso\CurrencyConverter;

    $service = new TrivialService();
    $peso = new CurrencyConverter($service);

    echo $peso->convert('123.45', 'EUR', 'EUR', 2), PHP_EOL; // 123.45

.. _builtin_reversible:

ReversibleService
=================

``\Peso\Core\Services\ReversibleService``

.. note::
    Values returned by a Reversible Service are calculated and therefore informational only.
    Never use them for precise conversions.

In case a service defines only a single base or quote currency,
Reversible Service can make it bi-directional by calculating a reverse value::

    <?php

    use Peso\Core\Services\ReversibleService;
    use Peso\Peso\CurrencyConverter;
    use Peso\Services\EuropeanCentralBankService;

    $converter = new CurrencyConverter(
        new ReversibleService(new EuropeanCentralBankService())
    );

    echo $converter->convertOnDate('123.45', 'USD', 'EUR', 2, '2025-06-13'); // 107.24

IndirectExchangeService
=======================

``\Peso\Core\Services\IndirectExchangeService``

.. note::
    Values returned by an Indirect Exchange Service are calculated and therefore informational only.
    Never use them for precise conversions.

In case a service defines only conversion rates back and forth for a single currency,
Indirect Exchange Service can make it every-to-every by using the selected currency as an intermediary::

    <?php

    use Peso\Core\Services\IndirectExchangeService;
    use Peso\Core\Services\ReversibleService;
    use Peso\Peso\CurrencyConverter;
    use Peso\Services\EuropeanCentralBankService;

    $converter = new CurrencyConverter(
        new IndirectExchangeService(
            new ReversibleService( // To and from EUR
                new EuropeanCentralBankService(), // Only EUR base
            ),
            'EUR',
        ),
    );

    // USD -> EUR -> PLN
    echo $converter->convertOnDate('123.45', 'USD', 'PLN', 2, '2025-06-13'); // 458.38

.. _builtin_conversion:

ConversionService
=================

.. versionadded:: 1.1

``\Peso\Core\Services\ConversionService``

Accepts an instance of ``CurrentConversionRequest`` / ``HistoricalConversionRequest``
and calculates the conversion amount by sending ``CurrentExchangeRateRequest`` / ``HistoricalConversionRequest``
to a wrapped service::

    <?php

    use Peso\Core\Requests\CurrentConversionRequest;
    use Peso\Core\Services\ConversionService;
    use Peso\Core\Types\Decimal;
    use Peso\Services\EuropeanCentralBankService;

    $service = new ConversionService(new EuropeanCentralBankService());

    echo $service->send(
        new CurrentConversionRequest(new Decimal('123.45'), 'EUR', 'PHP')
    )->amount->value; // 8167.57545 (2025-06-30)

ArrayService
============

``\Peso\Core\Services\ArrayService($currentRates = [], $historicalRates = [])``

Array Service holds static exchange rates::

    <?php

    use Peso\Core\Services\ArrayService;
    use Peso\Peso\CurrencyConverter;

    $service = new ArrayService(
        currentRates: [
            // Base Currencies
            'EUR' => [
                // Quote => rate
                'USD' => '1.12',
            ],
        ],
        historicalRates: [
            // Y-m-d dates
            '2025-06-13' => [
                // Base Currencies
                'EUR' => [
                    // Quote => rate
                    'USD' => '1.09',
                ],
            ],
        ]
    );
    $converter = new CurrencyConverter($service);

    echo
        $converter->convert('150.00', 'EUR', 'USD', 2), PHP_EOL, // 168.00
        $converter->convertOnDate('150.00', 'EUR', 'USD', 2, '2025-06-13'), PHP_EOL; // 163.50

Callback Service
================

.. versionadded:: 1.3

``\Peso\Core\Services\CallbackService``

Callback service is a wrapper for a closure to quickly create a simple test service::

    <?php

    use Arokettu\Date\Date;
    use Peso\Core\Exceptions\RequestNotSupportedException;
    use Peso\Core\Requests\CurrentExchangeRateRequest;
    use Peso\Core\Responses\ErrorResponse;
    use Peso\Core\Responses\ExchangeRateResponse;
    use Peso\Core\Services\CallbackService;
    use Peso\Core\Types\Decimal;
    use Peso\Peso\CurrencyConverter;

    require __DIR__ . '/vendor/autoload.php';

    $peso = new CurrencyConverter(new CallbackService(function ($request) {
        if (
            $request instanceof CurrentExchangeRateRequest &&
            $request->quoteCurrency === 'GBP' &&
            $request->baseCurrency === 'EUR'
        ) {
            return new ExchangeRateResponse(Decimal::init('1.5'), Date::today());
        }

        return new ErrorResponse(RequestNotSupportedException::fromRequest($request));
    }));

    echo $peso->convert('1200', 'EUR', 'GBP', 2); // 1800.00

NullService
===========

``\Peso\Core\Services\NullService``

Null Service fails every request, may be useful for testing purposes::

    <?php

    use Peso\Core\Services\NullService;
    use Peso\Peso\CurrencyConverter;

    $converter = new CurrencyConverter(new NullService());

    // Peso\Core\Exceptions\RequestNotSupportedException
    $converter->convert('100', 'USD', 'EUR', 2);
