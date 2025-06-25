.. _exchanger_interop:

Exchanger and Swap
##################

.. highlight:: php

Interoperability package for Exchanger_ and Swap_.

.. _Exchanger: https://florianv.github.io/exchanger/
.. _Swap: https://florianv.github.io/swap/

Installation
============

.. code-block:: bash

    composer install peso/peso-exchanger-interop

Usage
=====

The library is essentially 2 classes:

* ``\Peso\Exchanger\Interop\ExchangerService`` wraps Peso services to be used in Exchanger
* ``\Peso\Exchanger\Interop\PesoService`` wraps Exchanger services to be used in Peso

Peso services in Exchanger
--------------------------

Create a Peso service and pass it to Exchanger::

    <?php

    use Exchanger\Exchanger;
    use Exchanger\ExchangeRateQueryBuilder;
    use Peso\Exchanger\Interop\ExchangerService;
    use Peso\Services\EuropeanCentralBankService;

    $service = new ExchangerService(new EuropeanCentralBankService());
    $exchanger = new Exchanger($service);

    $query = (new ExchangeRateQueryBuilder('EUR/USD'))
        ->setDate(new DateTimeImmutable('2025-06-13'))
        ->build();

    $rate = $exchanger->getExchangeRate($query);

    echo $rate->getValue(), PHP_EOL; // 1.1512

Peso services in Swap
---------------------

Swap is a library that wraps Exchanger so it works too::

    <?php

    use Peso\Exchanger\Interop\ExchangerService;
    use Peso\Services\EuropeanCentralBankService;
    use Swap\Builder;

    $service = new ExchangerService(new EuropeanCentralBankService());
    $swap = (new Builder())
        ->addExchangeRateService($service)
        ->build();

    $rate = $swap->historical('EUR/USD', new DateTimeImmutable('2025-06-13'));

    echo $rate->getValue(), PHP_EOL; // 1.1512

Exchanger services in Peso
--------------------------

Create an Exchanger service and pass it to Peso::

    <?php

    use Exchanger\Service\EuropeanCentralBank;
    use Peso\Exchanger\Interop\PesoService;
    use Peso\Peso\CurrencyConverter;

    $service = new PesoService(new EuropeanCentralBank());
    $peso = new CurrencyConverter($service);

    // 1.1512
    echo $peso->getHistoricalConversionRate('EUR', 'USD', '2025-06-13'), PHP_EOL;

Caching
=======

Caching can be tricky due to design differences of Peso and Exchanger.
In Peso, caching is a responsibility of a Service.
In Exchanger, caching is a responsibility of the Exchanger itself.

* When using Exchanger or Swap with Peso services, a cache can be set on either side or even both::

    <?php

    use Peso\Exchanger\Interop\ExchangerService;
    use Peso\Services\EuropeanCentralBankService;
    use Swap\Builder;
    use Symfony\Component\Cache\Adapter\FilesystemAdapter;
    use Symfony\Component\Cache\Psr16Cache;

    $cache = new Psr16Cache(new FilesystemAdapter(/* ... */));
    $service = new ExchangerService(
        // Peso-side cache
        new EuropeanCentralBankService($cache)
    );

    $exchanger = new Exchanger($service, $cache); // Exchanger-side cache
    // or
    $swap = (new Builder())
        ->addExchangeRateService($service)
        ->useSimpleCache($cache) // Swap-side cache
        ->build();

* When using Peso with Exchanger services, the only place to set up a cache is the wrapper itself::

    <?php

    use Exchanger\Service\EuropeanCentralBank;
    use Peso\Exchanger\Interop\PesoService;
    use Peso\Peso\CurrencyConverter;
    use Symfony\Component\Cache\Adapter\FilesystemAdapter;
    use Symfony\Component\Cache\Psr16Cache;

    $cache = new Psr16Cache(new FilesystemAdapter(/* ... */));
    $service = new PesoService(new EuropeanCentralBank(), $cache);
    $peso = new CurrencyConverter($service);
