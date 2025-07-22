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

Example::

    <?php

    use Peso\Peso\CurrencyConverter;
    use Peso\Services\CzechNationalBankService;
    use Symfony\Component\Cache\Adapter\FilesystemAdapter;
    use Symfony\Component\Cache\Psr16Cache;

    $cache = new Psr16Cache(new FilesystemAdapter(directory: __DIR__ . '/cache'));
    $service = new CzechNationalBankService($cache);
    $converter = new CurrencyConverter($service);

    // 310812.50 as of 2025-06-23
    echo $converter->convert('12500', 'EUR', 'CZK', 2), PHP_EOL;

    // reversible (wraps service with ReversibleService)

    $service = CzechNationalBankService::reversible($cache);
    $converter = new CurrencyConverter($service);

    // 502.71 as of 2025-06-23
    echo $converter->convert('12500', 'CZK', 'EUR', 2), PHP_EOL;

.. note::
    Reversible Factory emits non-precise services
    that can only be used in informational purposes.
