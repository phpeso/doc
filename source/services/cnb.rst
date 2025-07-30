.. _cnb_service:

Czech National Bank
###################

.. highlight:: php

This service retrieves the data from `the Czech National Bank <cnb_>`_.

.. _cnb: https://www.cnb.cz/en/financial-markets/foreign-exchange-market/central-bank-exchange-rate-fixing/central-bank-exchange-rate-fixing/

Installation
============

Install the service:

.. code-block:: bash

    composer require peso/cnb-service

Install the service with all recommended dependencies:

.. code-block:: bash

    composer require peso/cnb-service php-http/discovery guzzlehttp/guzzle symfony/cache

Usage
=====

.. versionchanged:: 1.1 ``CzechNationalBankService`` -> ``CzechNationalBank\CentralBankFixingService``
.. versionadded:: 1.1 ``OtherCurrenciesService``

The package provides 2 Service objects:

* ``\Peso\Services\CzechNationalBank\CentralBankFixingService``: Central bank exchange rate fixing data (daily rates)
* ``\Peso\Services\CzechNationalBank\OtherCurrenciesService``: FX rates of other currencies (monthly rates)

Example::

    <?php

    use Peso\Peso\CurrencyConverter;
    use Peso\Services\CzechNationalBank\CentralBankFixingService;
    use Symfony\Component\Cache\Adapter\FilesystemAdapter;
    use Symfony\Component\Cache\Psr16Cache;

    $cache = new Psr16Cache(new FilesystemAdapter(directory: __DIR__ . '/cache'));
    $service = new CentralBankFixingService($cache);
    $converter = new CurrencyConverter($service);

    // 310812.50 as of 2025-06-23
    echo $converter->convert('12500', 'EUR', 'CZK', 2), PHP_EOL;

    // reversible (wraps service with ReversibleService)

    $service = CentralBankFixingService::reversible($cache);
    $converter = new CurrencyConverter($service);

    // 502.71 as of 2025-06-23
    echo $converter->convert('12500', 'CZK', 'EUR', 2), PHP_EOL;

.. note::
    Reversible Factory emits non-precise services
    that can only be used in informational purposes.
