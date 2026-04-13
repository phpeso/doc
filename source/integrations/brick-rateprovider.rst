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

``Peso\Brick\PesoRateProvider`` provides a wrapper for both current and historical convertion rates.

::

    <?php

    use Brick\Money\CurrencyConverter;
    use Brick\Money\Money;
    use Peso\Brick\PesoRateProvider;
    use Peso\Services\EuropeanCentralBankService;

    $rateProvider = new PesoRateProvider(new EuropeanCentralBankService());
    $converter = new CurrencyConverter($rateProvider);

    $eur100 = Money::of('100.00', 'EUR');

    echo $converter->convert($eur100, 'USD'), PHP_EOL; // 'USD ...'

    // or

    echo $converter->convert($eur100, 'USD', [
        'date' => '2025-06-13',
    ]), PHP_EOL; // 'USD 115.12'

.. seealso:: `See more on the Brick\\Money doc page`__.

.. __: https://github.com/brick/money/blob/master/README.md#currency-conversion

Upgrade
=======

1.x to 2.0
----------

* Due to huge difference between brick/money 0.12 and 0.13 a major release was required
* ``PesoHistoricalRateProvider`` became obsolete and is soft-deprecated::

        <?php

        use Arokettu\Date\Calendar;
        use Brick\Money\CurrencyConverter;
        use Brick\Money\Money;
        use Peso\Brick\PesoHistoricalRateProvider;
        use Peso\Brick\PesoRateProvider;
        use Peso\Services\EuropeanCentralBankService;

        $eur100 = Money::of('100.00', 'EUR');

        // 1.x

        // a dedicated provider
        $rateProvider = new PesoHistoricalRateProvider(
            new EuropeanCentralBankService(),
            Calendar::parse('2025-06-13'),
        );
        $converter = new CurrencyConverter($rateProvider);

        echo $converter->convert($eur100, 'USD'), PHP_EOL; // 'USD 115.12'

        // 2.x

        // a regular provider
        $rateProvider = new PesoRateProvider(new EuropeanCentralBankService());
        $converter = new CurrencyConverter($rateProvider);

        echo $converter->convert($eur100, 'USD', [
            'date' => '2025-06-13',
        ]), PHP_EOL; // 'USD 115.12'
