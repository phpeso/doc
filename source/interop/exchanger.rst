.. _exchanger_interop:

Exchanger and Swap
##################

.. highlight:: php

Interoperability package for Exchanger_ and Swap_.
Since version 1.0.2 it is possible to use this package with compatible Exchange forks like `part-db/exchanger <pdbexchanger_>`__,
however it is not officially supported.

.. _Exchanger: https://florianv.github.io/exchanger/
.. _Swap: https://florianv.github.io/swap/
.. _pdbexchanger: https://packagist.org/packages/part-db/exchanger

Installation
============

.. versionchanged:: 1.0.2 florianv/exchanger is no longer an explicit dependency of this package

.. code-block:: bash

    composer require peso/peso-exchanger-interop florianv/exchanger

Usage
=====

.. versionchanged:: 1.1.0 Namespace change: ``Peso\Exchanger\Interop`` → ``Peso\Interop\Exchanger``

The library is essentially 2 classes:

* ``\Peso\Interop\Exchanger\ExchangerService`` wraps Peso services to be used in Exchanger
* ``\Peso\Interop\Exchanger\PesoService`` wraps Exchanger services to be used in Peso

Peso services in Exchanger
--------------------------

Create a Peso service and pass it to Exchanger::

    <?php

    use Exchanger\Exchanger;
    use Exchanger\ExchangeRateQueryBuilder;
    use Peso\Interop\Exchanger\ExchangerService;
    use Peso\Services\EuropeanCentralBankService;

    $service = new ExchangerService(new EuropeanCentralBankService());
    $exchanger = new Exchanger($service);

    $query = (new ExchangeRateQueryBuilder('EUR/USD'))
        ->setDate(new DateTimeImmutable('2025-06-13'))
        ->build();

    $rate = $exchanger->getExchangeRate($query);

    echo $rate->getValue(), PHP_EOL; // 1.1512

Peso services in Swap
---------------------

Swap is a library that wraps Exchanger so it works too::

    <?php

    use Peso\Interop\Exchanger\ExchangerService;
    use Peso\Services\EuropeanCentralBankService;
    use Swap\Builder;

    $service = new ExchangerService(new EuropeanCentralBankService());
    $swap = (new Builder())
        ->addExchangeRateService($service)
        ->build();

    $rate = $swap->historical('EUR/USD', new DateTimeImmutable('2025-06-13'));

    echo $rate->getValue(), PHP_EOL; // 1.1512

Exchanger services in Peso
--------------------------

Create an Exchanger service and pass it to Peso::

    <?php

    use Exchanger\Service\EuropeanCentralBank;
    use Peso\Interop\Exchanger\PesoService;
    use Peso\Peso\CurrencyConverter;

    $service = new PesoService(new EuropeanCentralBank());
    $peso = new CurrencyConverter($service);

    // 1.1512
    echo $peso->getHistoricalConversionRate('EUR', 'USD', '2025-06-13'), PHP_EOL;

Caching
=======

Caching can be tricky due to design differences of Peso and Exchanger.
In Peso, caching is a responsibility of a Service.
In Exchanger, caching is a responsibility of the Exchanger itself.

* When using Exchanger or Swap with Peso services, a cache can be set on either side or even both::

    <?php

    use Peso\Interop\Exchanger\ExchangerService;
    use Peso\Services\EuropeanCentralBankService;
    use Swap\Builder;
    use Symfony\Component\Cache\Adapter\FilesystemAdapter;
    use Symfony\Component\Cache\Psr16Cache;

    $cache = new Psr16Cache(new FilesystemAdapter(/* ... */));
    $service = new ExchangerService(
        // Peso-side cache
        new EuropeanCentralBankService($cache)
    );

    $exchanger = new Exchanger($service, $cache); // Exchanger-side cache
    // or
    $swap = (new Builder())
        ->addExchangeRateService($service)
        ->useSimpleCache($cache) // Swap-side cache
        ->build();

* When using Peso with Exchanger services, the only place to set up a cache is the wrapper itself::

    <?php

    use Exchanger\Service\EuropeanCentralBank;
    use Peso\Interop\Exchanger\PesoService;
    use Peso\Peso\CurrencyConverter;
    use Symfony\Component\Cache\Adapter\FilesystemAdapter;
    use Symfony\Component\Cache\Psr16Cache;

    $cache = new Psr16Cache(new FilesystemAdapter(/* ... */));
    $service = new PesoService(new EuropeanCentralBank(), $cache);
    $peso = new CurrencyConverter($service);
