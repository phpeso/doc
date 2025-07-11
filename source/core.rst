.. _core:

Advanced Usage
##############

.. highlight:: php

In case you need to use all power of Peso, you can use the core directly.

Installation
============

Depend on ``peso/core`` if you are creating an integration:

.. code-block:: bash

    composer require peso/core

If you just want to use services directly, just install the service you need, ECB for example:

.. code-block:: bash

    composer require peso/ecb-service php-http/discovery guzzlehttp/guzzle symfony/cache

.. _model:

Model
=====

Services operate on request/response model.

..  list-table::
    :header-rows: 1

    *   * Action
        * Request
        * Response
    *   * Current exchange rate
        * ``CurrentExchangeRateRequest``
        * ``ExchangeRateResponse`` or ``ErrorResponse``
    *   * Historical exchange rate
        * ``HistoricalExchangeRateRequest``
        * ``ExchangeRateResponse`` or ``ErrorResponse``
    *   * Conversion by the current rate
        * ``CurrentConversionRequest``
        * ``ConversionResponse`` or ``ErrorResponse``
    *   * Conversion by a historical rate
        * ``HistoricalConversionRequest``
        * ``ConversionResponse`` or ``ErrorResponse``
    *   * Future scope and invalid classes
        * any other object
        * ``ErrorResponse``

Exchange Rates
==============

* ``\Peso\Core\Requests\CurrentExchangeRateRequest`` queries the currently active exchange rates.
* ``\Peso\Core\Requests\HistoricalExchangeRateRequest`` queries exchange rates on a specific date.

Examples::

    <?php

    use Arokettu\Date\Calendar;
    use Peso\Core\Requests\CurrentExchangeRateRequest;
    use Peso\Core\Requests\HistoricalExchangeRateRequest;
    use Peso\Services\EuropeanCentralBankService;

    $service = new EuropeanCentralBankService();

    //  {
    //      value => Decimal("66.161")
    //      date => Date("2025-06-30")
    //  }
    var_dump(
        $service->send(new CurrentExchangeRateRequest('EUR', 'PHP'))
    );

    //  {
    //      value => Decimal("64.706")
    //      // there are no rates for Sunday, so the returned rates are from Friday
    //      // not all services provide the date correctly
    //      date => Date("2025-06-13")
    //  }
    var_dump(
        $service->send(new HistoricalExchangeRateRequest('EUR', 'PHP', Calendar::parse('2025-06-15')))
    );

Conversion
==========

* ``\Peso\Core\Requests\CurrentConversionRequest`` converts currencies by current conversion rates.
* ``\Peso\Core\Requests\HistoricalConversionRequest`` converts currencies a conversion rate on a given date.

Some services support conversion natively (Fixer, for example),
other services can be wrapped with the :ref:`ConversionService <builtin_conversion>`::

    <?php

    use Arokettu\Date\Calendar;
    use Peso\Core\Requests\CurrentConversionRequest;
    use Peso\Core\Requests\HistoricalConversionRequest;
    use Peso\Core\Services\ConversionService;
    use Peso\Core\Types\Decimal;
    use Peso\Services\EuropeanCentralBankService;

    $service = new ConversionService(new EuropeanCentralBankService());

    //  {
    //      amount => Decimal("8167.57545")
    //      date => Date("2025-06-30")
    //  }
    var_dump(
        $service->send(new CurrentConversionRequest(new Decimal('123.45'), 'EUR', 'PHP')
    ));

    //  {
    //      amount => Decimal("7987.95570")
    //      date => Date("2025-06-13")
    //  }
    var_dump(
        $service->send(new HistoricalConversionRequest(new Decimal('123.45'), 'EUR', 'PHP', Calendar::parse('2025-06-15'))
    ));

Data Types
==========

Specific data types used in this framework:

* ``\Peso\Core\Types\Decimal`` is a string wrapper over a decimal string that enforces its validity.
* ``\Arokettu\Date\Date`` is an object that represents a date without time and a time zone, see `arokettu/date`_.

.. _arokettu/date: https://php-date.readthedocs.io/
