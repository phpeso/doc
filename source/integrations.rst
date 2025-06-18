Integrations
############

.. highlight:: php

.. _peso_peso:

Peso Frontend
=============

.. code-block:: bash

    composer install peso/peso

.. _peso_moneyphp:

Money for PHP
=============

.. code-block:: bash

    composer install peso/moneyphp-exchange

This package provides integration with the `Money for PHP`_ library.

.. _Money for PHP: https://www.moneyphp.org/

There are two Exchange objects:

* PesoExchange (``\Peso\Money\PesoExchange``) provides a wrapper for current convertion rates.
* PesoExchange (``\Peso\Money\PesoHistoricalExchange``) provides a wrapper for historical convertion rates.

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

    require __DIR__ . '/vendor/autoload.php';

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

.. note:: `See more on the Money for PHP doc page`__.

.. __: https://www.moneyphp.org/en/stable/features/currency-conversion.html
