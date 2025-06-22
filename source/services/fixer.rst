.. _fixer_service:

Fixer
#####

.. highlight:: php

This service retrieves the data from `the Fixer.io service <fixer_>`_.

.. _fixer: https://fixer.io

Installation
============

Install the service:

.. code-block:: bash

    composer install peso/fixer-service

Install the service with all recommended dependencies:

.. code-block:: bash

    composer install peso/fixer-service php-http/discovery guzzlehttp/guzzle symfony/cache

Usage
=====

.. note::
    Free key allows you to retrieve only Euro as a base currency.
    To be able to convert other currencies back to EUR you can wrap it with :ref:`builtin_reversible`.

Example::

    <?php

    use Peso\Core\Services\ReversibleService;
    use Peso\Peso\CurrencyConverter;
    use Peso\Services\Fixer\AccessKeyType;
    use Peso\Services\FixerService;
    use Symfony\Component\Cache\Adapter\FilesystemAdapter;
    use Symfony\Component\Cache\Psr16Cache;

    require __DIR__ . '/vendor/autoload.php';

    $cache = new Psr16Cache(new FilesystemAdapter(directory: __DIR__ . '/cache'));
    $service = new FixerService('...', AccessKeyType::Free, cache: $cache);
    $converter = new CurrencyConverter($service);

    // 14419.61 as of 2025-06-20
    echo $converter->convert('12500', 'EUR', 'USD', 2), PHP_EOL;

    $reversibleService = new ReversibleService($service);
    $converter = new CurrencyConverter($reversibleService);

    // 10835.94 as of 2025-06-20
    echo $converter->convert('12500', 'USD', 'EUR', 2), PHP_EOL;

    // you can optionally limit the retrieved symbols
    $cache = new Psr16Cache(new FilesystemAdapter(directory: __DIR__ . '/cache'));
    $service = new FixerService('...', AccessKeyType::Free, [
        'EUR', 'USD', 'JPY', 'CHF'
    ], $cache);
    $converter = new CurrencyConverter($service);

    // ...
