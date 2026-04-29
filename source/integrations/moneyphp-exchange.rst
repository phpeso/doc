.. _peso_moneyphp:

Money for PHP
#############

This package provides integration with the `Money for PHP`_ library.

.. _Money for PHP: https://www.moneyphp.org/

.. highlight:: php

Installation
============

.. code-block:: bash

    composer require peso/moneyphp-exchange

Usage
=====

Exchange Objects
----------------

Exchange objects can be used with the ``Money\Exchange`` directly.
There are two Exchange objects:

* PesoExchange (``\Peso\Money\PesoExchange``) provides a wrapper for current convertion rates.
* PesoHistoricalExchange (``\Peso\Money\PesoHistoricalExchange``) provides a wrapper for historical convertion rates.

::

    <?php

    use Arokettu\Date\Calendar;
    use Money\Converter;
    use Money\Currencies\ISOCurrencies;
    use Money\Currency;
    use Money\Money;
    use Peso\Money\PesoExchange;
    use Peso\Money\PesoHistoricalExchange;
    use Peso\Services\EuropeanCentralBankService;

    $exchange = new PesoExchange(new EuropeanCentralBankService());
    $converter = new Converter(new ISOCurrencies(), $exchange);

    $eur100 = Money::EUR(10000);

    var_dump($converter->convert($eur100, new Currency('USD'))); // Money::USD(...)

    // or

    $exchange = new PesoHistoricalExchange(
        new EuropeanCentralBankService(),
        Calendar::parse('2025-06-13')
    );
    $converter = new Converter(new ISOCurrencies(), $exchange);

    $eur100 = Money::EUR(10000);

    var_dump($converter->convert($eur100, new Currency('USD'))); // Money::USD(11512)

Converter Wrapper
-----------------

.. versionadded:: 1.1

``Peso\Money\PesoConverter``

A convenience wrapper over the ``Money\Converter`` that can act as a drop-in replacement.
It simplifies querying of historical rates and exposes currency pair creation from the exchanges::

    <?php

    use Money\Currencies\ISOCurrencies;
    use Money\Currency;
    use Money\CurrencyPair;
    use Money\Money;
    use Peso\Money\PesoConverter;
    use Peso\Services\EuropeanCentralBankService;

    $converter = new PesoConverter(new ISOCurrencies(), new EuropeanCentralBankService());

    $eur100 = Money::EUR(10000);

    // like a base \Money\Converter

    // Money::USD(...)
    var_dump($converter->convert($eur100, new Currency('USD')));
    // [Money::USD(...), CurrencyPair(EUR/USD ...)]
    var_dump($converter->convertAndReturnWithCurrencyPair($eur100, new Currency('USD')));

    // historical helpers

    // Money::USD(11706)
    var_dump($converter->convertOnDate($eur100, new Currency('USD'), '2026-04-29'));
    // [Money::USD(11706), CurrencyPair(EUR/USD 1.1706)]
    var_dump($converter->convertAndReturnWithCurrencyPairOnDate(
        $eur100, new Currency('USD'), '2026-04-29',
    ));

    // currency pair creation

    // CurrencyPair(EUR/USD ...)
    var_dump($converter->quote(new Currency('EUR'), new Currency('USD')));
    // CurrencyPair(EUR/USD 1.1706)]
    var_dump($converter->quoteOnDate(new Currency('EUR'), new Currency('USD'), '2026-04-29'));

    // exchange agnostic method for completeness

    // Money::USD(12345)
    var_dump($converter->convertAgainstCurrencyPair(
        $eur100,
        CurrencyPair::createFromIso('EUR/USD 1.2345'),
    ));

.. seealso:: `See more on the Money for PHP doc page`__.

.. __: https://www.moneyphp.org/en/stable/features/currency-conversion.html
