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

.. versionadded:: 2.0 Conversion requests support

.. php:namespace:: Peso\Services
.. php:class:: CurrencyApiService

    The service

    .. php:method:: __construct($apiKey, $subscription, [$symbols, $multiconversion, [$cache, $ttl, $httpClient, $requestFactory]])

        Required params:

        :param string $apiKey: The API key you received from the service.
        :param Subscription $subscription: Subscription type, Free or Paid.

        Configuration:

        :param array|null $symbols:
            Use this list to limit currencies in the query (limits only quote/target currencies)
            Default: ``null`` queries all currencies.
        :param bool $multiconversion:
            Enable if you need to convert a single amount of a single currency to multiple currenices.
            The service will ask the backend to get result for all currencies (controlled by ``$symbols``)
            and the subsequent requests will get results from the cache.
            Only valid for conversion requests and requires caching enabled.
            Default: ``false``.

        Services:

        :param CacheInterface $cache: PSR-16 Cache Instance. Default: no cache (not recommended).
        :param DateInterval $ttl: Cache TTL. Default: ``1 hour``.
        :param ClientInterface $httpClient: PSR-18 Client Instance.
            Default: something discovered (requires ``php-http/discovery`` and an implementation installed).
        :param RequestFactoryInterface $requestFactory: PSR-17 RequestFactory Instance.
            Default: something discovered (requires ``php-http/discovery`` and an implementation installed).

.. php:namespace:: Peso\Services\CurrencyApiService
.. php:enum:: Subscrtiption

    .. php:const:: Free

        Free subscription (no conversion requests)
    .. php:const:: Paid

        Any type of paid subscription (conversion requests)

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

Upgrade
=======

1.x to 2.x
----------

* An extra parameter, ``$multiconversion`` was added to the constructor.
  If you are not using named parameters, you need to account for that.
