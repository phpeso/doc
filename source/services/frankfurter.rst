.. _frankfurter_service:

Frankfurter.dev
###############

.. highlight:: php

This service retrieves the data from `Frankfurter.dev <ffdev_>`_.

.. _ffdev: https://frankfurter.dev/

Installation
============

Install the service:

.. code-block:: bash

    composer require peso/frankfurter-service

Install the service with all recommended dependencies:

.. code-block:: bash

    composer require peso/frankfurter-service php-http/discovery guzzlehttp/guzzle symfony/cache

Usage
=====

Example::

    <?php

    use Peso\Peso\CurrencyConverter;
    use Peso\Services\FrankfurterService;
    use Symfony\Component\Cache\Adapter\FilesystemAdapter;
    use Symfony\Component\Cache\Psr16Cache;

    $cache = new Psr16Cache(new FilesystemAdapter(directory: __DIR__ . '/cache'));
    $service = new FrankfurterService(cache: $cache);
    $converter = new CurrencyConverter($service);

    // 10664.00 as of 2025-12-18
    echo $converter->convert('12500', 'USD', 'EUR', 2), PHP_EOL;

    // use a self hosted version
    $service = new FrankfurterService(hostname: 'http://localhost:8080', cache: $cache);
