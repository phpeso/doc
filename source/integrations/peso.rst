.. _peso_peso:

Peso Currency Converter
#######################

.. highlight:: php

A simple standalone currency converter.

Installation
============

.. code-block:: bash

    composer install peso/peso

Usage
=====

Peso returns numeric strings that can be used with various decimal calculation libraries like BcMath
or, for example, with Money's `Teller object`__.

.. __: https://www.moneyphp.org/en/stable/features/teller.html

Initialize it with a service provider::

    <?php

    use Peso\Peso\CurrencyConverter;
    use Peso\Services\EuropeanCentralBankService;

    $peso = new CurrencyConverter(new EuropeanCentralBankService());

Query rates::

    <?php

    use Peso\Peso\CurrencyConverter;
    use Peso\Services\EuropeanCentralBankService;

    $peso = new CurrencyConverter(new EuropeanCentralBankService());

    // current
    echo $peso->getConversionRate(
        'EUR', // base
        'PHP', // quote
    ), PHP_EOL;
    // and historical
    echo $peso->getHistoricalConversionRate(
        'EUR', // base
        'PHP', // quote
        '2025-06-13', // date (Y-m-d string or DateTime or arokettu/date Date)
    ), PHP_EOL; // '64.706'

Convert currency amounts::

    <?php

    use Peso\Peso\CurrencyConverter;
    use Peso\Services\EuropeanCentralBankService;

    $peso = new CurrencyConverter(new EuropeanCentralBankService());

    // current
    echo $peso->convert(
        '1500.00', // amount. Numeric string (recommended) or float (not recommended)
        'EUR', // base
        'PHP', // quote
        2, // quote precision. Philippine peso is divided into 100 sentimo
    ), PHP_EOL;
    // and historical
    echo $peso->convertOnDate(
        '1500.00', // amount. Numeric string (recommended) or float (not recommended)
        'EUR', // base
        'PHP', // quote
        2, // quote precision. Philippine peso is divided into 100 sentimo
        '2025-06-13'
    ), PHP_EOL; // '97059.00'

.. note::
    Peso does not store a list of currencies so you need to specify amount precision manually.
    If you want this to happen automatically,
    please use `Money for PHP`__ with :ref:`the corresponding integration <peso_moneyphp>`.

.. __: https://www.moneyphp.org/
