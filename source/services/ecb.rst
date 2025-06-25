.. _ecb_service:

European Central Bank
#####################

.. highlight:: php

This service retrieves the data from `the European Central Bank <ecb_>`_.

.. _ecb: https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html

Installation
============

Install the service:

.. code-block:: bash

    composer require peso/ecb-service

Install the service with all recommended dependencies:

.. code-block:: bash

    composer require peso/ecb-service php-http/discovery guzzlehttp/guzzle symfony/cache

Usage
=====

Example::

    <?php

    use Peso\Peso\CurrencyConverter;
    use Peso\Services\EuropeanCentralBankService;
    use Symfony\Component\Cache\Adapter\FilesystemAdapter;
    use Symfony\Component\Cache\Psr16Cache;

    $cache = new Psr16Cache(new FilesystemAdapter(directory: __DIR__ . '/cache'));
    $service = new EuropeanCentralBankService($cache);
    $converter = new CurrencyConverter($service);

    // 14347.50 as of 2025-06-19
    echo $converter->convert('12500', 'EUR', 'USD', 2), PHP_EOL;

    // reversible (wraps service with ReversibleService)

    $service = EuropeanCentralBankService::reversible($cache);
    $converter = new CurrencyConverter($service);

    // 10890.40 as of 2025-06-19
    echo $converter->convert('12500', 'USD', 'EUR', 2), PHP_EOL;

    // universal (wraps service with IndirectExchangeService)

    $service = EuropeanCentralBankService::universal($cache);
    $converter = new CurrencyConverter($service);

    // 270299.70 as of 2025-06-19
    echo $converter->convert('12500', 'USD', 'CZK', 2), PHP_EOL;

.. note::
    Using this service without a properly set up cache is strongly discouraged
    and may lead to a poor performance.

.. warning::
    Universal and Reversible factories emit non-precise services
    that can only be used in informational purposes.
