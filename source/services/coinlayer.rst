.. _coinlayer_service:

Coinlayer
#########

.. highlight:: php

This service retrieves the data from `Coinlayer <coin_>`_.

.. _coin: https://coinlayer.com/

Installation
============

Install the service:

.. code-block:: bash

    composer require peso/coinlayer-service

Install the service with all recommended dependencies:

.. code-block:: bash

    composer require peso/coinlayer-service php-http/discovery guzzlehttp/guzzle symfony/cache

Usage
=====

Example::

    <?php

    use Peso\Peso\CurrencyConverter;
    use Peso\Services\Coinlayer\AccessKeyType;
    use Peso\Services\CoinlayerService;
    use Symfony\Component\Cache\Adapter\FilesystemAdapter;
    use Symfony\Component\Cache\Psr16Cache;

    $cache = new Psr16Cache(new FilesystemAdapter(directory: __DIR__ . '/cache'));
    // You need a reversible service to get fiat to crypto rates (only crypto to fiat is supported by the service)
    $service = CoinlayerService::reversible('...', AccessKeyType::Free, cache: $cache);
    $converter = new CurrencyConverter($service);

    // 6.91 as of 2026-04-06
    echo $converter->convert('12500', 'USD', 'ETH', 2), PHP_EOL;
