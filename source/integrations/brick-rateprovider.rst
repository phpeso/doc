.. _peso_brick:

Brick\\Money
############

This package provides integration with the `Brick\\Money`_ library.

.. _Brick\\Money: https://github.com/brick/money

.. highlight:: php

Installation
============

.. code-block:: bash

    composer require peso/brick-rateprovider

Usage
=====

There are two RateProvider objects:

* PesoExchange (``\Peso\Brick\PesoRateProvider``) provides a wrapper for current convertion rates.
* PesoHistoricalExchange (``\Peso\Brick\PesoHistoricalRateProvider``) provides a wrapper for historical convertion rates.

::

    <?php

    use Arokettu\Date\Calendar;
    use Brick\Money\CurrencyConverter;
    use Brick\Money\Money;
    use Peso\Brick\PesoHistoricalRateProvider;
    use Peso\Brick\PesoRateProvider;
    use Peso\Services\EuropeanCentralBankService;

    require __DIR__ . '/vendor/autoload.php';

    $rateProvider = new PesoRateProvider(new EuropeanCentralBankService());
    $converter = new CurrencyConverter($rateProvider);

    $eur100 = Money::of('100.00', 'EUR');

    echo $converter->convert($eur100, 'USD'), PHP_EOL; // 'USD ...'

    // or

    $rateProvider = new PesoHistoricalRateProvider(
        new EuropeanCentralBankService(),
        Calendar::parse('2025-06-13')
    );
    $converter = new CurrencyConverter($rateProvider);

    $eur100 = Money::of('100.00', 'EUR');

    echo $converter->convert($eur100, 'USD'), PHP_EOL; // 'USD 115.12'

.. seealso:: `See more on the Brick\\Money doc page`__.

.. __: https://github.com/brick/money/blob/master/README.md#currency-conversion
