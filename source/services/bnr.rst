.. _bnr_service:

National Bank of Romania
########################

.. highlight:: php

This service retrieves the data from `the National Bank of Romania <bnr_>`_.

.. _bnr: https://www.bnr.ro/en/24006-exchange-rate-list-in-xml-format

Installation
============

Install the service:

.. code-block:: bash

    composer require peso/bnr-service

Install the service with all recommended dependencies:

.. code-block:: bash

    composer require peso/bnr-service php-http/discovery guzzlehttp/guzzle symfony/cache

Usage
=====

Example::

    <?php

    use Peso\Peso\CurrencyConverter;
    use Peso\Services\NationalBankOfRomaniaService;
    use Symfony\Component\Cache\Adapter\FilesystemAdapter;
    use Symfony\Component\Cache\Psr16Cache;

    $cache = new Psr16Cache(new FilesystemAdapter(directory: __DIR__ . '/cache'));
    $service = new NationalBankOfRomaniaService($cache);
    $converter = new CurrencyConverter($service);

    // 63465.00 as of 2025-09-26
    echo $converter->convert('12500', 'EUR', 'RON', 2), PHP_EOL;

    // reversible (wraps service with ReversibleService)

    $service = NationalBankOfRomaniaService::reversible($cache);
    $converter = new CurrencyConverter($service);

    // 2461.99 as of 2025-09-26
    echo $converter->convert('12500', 'RON', 'EUR', 2), PHP_EOL;

    // universal (wraps service with IndirectExchangeService)

    $service = NationalBankOfRomaniaService::universal($cache);
    $converter = new CurrencyConverter($service);

    // 259928.23 as of 2025-09-26
    echo $converter->convert('12500', 'USD', 'CZK', 2), PHP_EOL;

.. warning::
    Using this service without a properly set up cache is strongly discouraged
    and may lead to a poor performance.

.. note::
    Universal and Reversible factories emit non-precise services
    that can only be used in informational purposes.
