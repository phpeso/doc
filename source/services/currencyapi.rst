.. _currencyapi_service:

CurrencyAPI
###########

.. highlight:: php

This service retrieves the data from `CurrencyAPI <cur_>`_.

.. _cur: https://currencyapi.com/

Installation
============

Install the service:

.. code-block:: bash

    composer require peso/currencyapi-service

Install the service with all recommended dependencies:

.. code-block:: bash

    composer require peso/currencyapi-service php-http/discovery guzzlehttp/guzzle symfony/cache

Usage
=====

Example::

    <?php

    use Peso\Peso\CurrencyConverter;
    use Peso\Services\CurrencyApiService;
    use Peso\Services\CurrencyApiService\Subscription;
    use Symfony\Component\Cache\Adapter\FilesystemAdapter;
    use Symfony\Component\Cache\Psr16Cache;

    $cache = new Psr16Cache(new FilesystemAdapter(directory: __DIR__ . '/cache'));
    $service = new CurrencyApiService('...', Subscription::Free, cache: $cache);
    $converter = new CurrencyConverter($service);

    // 10760.13 as of 2025-07-18
    echo $converter->convert('12500', 'USD', 'EUR', 2), PHP_EOL;

    // you can optionally limit the retrieved symbols
    $cache = new Psr16Cache(new FilesystemAdapter(directory: __DIR__ . '/cache'));
    $service = new CurrencyApiService('...', Subscription::Free, [
        'EUR', 'USD', 'JPY', 'CHF'
    ], $cache);
    $converter = new CurrencyConverter($service);

    // ...
