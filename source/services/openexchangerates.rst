.. _openexchangerates_service:

Open Exchange Rates
###################

.. highlight:: php

This service retrieves the data from `Open Exchange Rates <oxr_>`_.

.. _oxr: https://openexchangerates.org/

Installation
============

Install the service:

.. code-block:: bash

    composer require peso/openexchangerates-service

Install the service with all recommended dependencies:

.. code-block:: bash

    composer require peso/openexchangerates-service php-http/discovery guzzlehttp/guzzle symfony/cache

Usage
=====

.. hint::
    Free key allows you to retrieve only US Dollar as a base currency.
    To be able to convert other currencies back to USD you can wrap it with :ref:`builtin_reversible`.

Example::

    <?php

    use Peso\Core\Services\ReversibleService;
    use Peso\Peso\CurrencyConverter;
    use Peso\Services\OpenExchangeRatesService;
    use Peso\Services\OpenExchangeRatesService\AppType;
    use Symfony\Component\Cache\Adapter\FilesystemAdapter;
    use Symfony\Component\Cache\Psr16Cache;

    $cache = new Psr16Cache(new FilesystemAdapter(directory: __DIR__ . '/cache'));
    $service = new OpenExchangeRatesService('...', AppType::Free, cache: $cache);
    $converter = new CurrencyConverter($service);

    // 10664.96 as of 2025-06-26
    echo $converter->convert('12500', 'USD', 'EUR', 2), PHP_EOL;

    $reversibleService = new ReversibleService($service);
    $converter = new CurrencyConverter($reversibleService);

    // 14650.78 as of 2025-06-26
    echo $converter->convert('12500', 'EUR', 'USD', 2), PHP_EOL;

    // you can optionally limit the retrieved symbols
    $cache = new Psr16Cache(new FilesystemAdapter(directory: __DIR__ . '/cache'));
    $service = new OpenExchangeRatesService('...', AppType::Free, [
        'EUR', 'USD', 'JPY', 'CHF'
    ], $cache);
    $converter = new CurrencyConverter($service);

    // ...
