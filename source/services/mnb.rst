.. _mnb_service:

Hungarian National Bank
#######################

.. highlight:: php

This service retrieves the data from `the Hungarian National Bank (Magyar Nemzeti Bank) <mnb_>`_.

.. _mnb: https://www.mnb.hu/statisztika/statisztikai-adatok-informaciok/adatok-idosorok/arfolyamok-lekerdezese/aktualis-es-a-regebbi-arfolyamok-webszolgaltatasanak-dokumentacioja

Installation
============

Install the service:

.. code-block:: bash

    composer require peso/mnb-service

Install the service with all recommended dependencies:

.. code-block:: bash

    composer require peso/mnb-service symfony/cache

This library also requires the |soap|_ extension.

.. _soap: https://www.php.net/manual/en/book.soap.php
.. |soap| replace:: ``soap``

Usage
=====

Example::

    <?php

    use Peso\Peso\CurrencyConverter;
    use Peso\Services\HungarianNationalBankService;
    use Symfony\Component\Cache\Adapter\FilesystemAdapter;
    use Symfony\Component\Cache\Psr16Cache;

    $cache = new Psr16Cache(new FilesystemAdapter(directory: __DIR__ . '/cache'));
    $service = new HungarianNationalBankService($cache);
    $converter = new CurrencyConverter($service);

    // 4771875 as of 2025-11-27
    echo $converter->convert('12500', 'EUR', 'HUF', 0), PHP_EOL;

    // reversible (wraps service with ReversibleService)

    $service = HungarianNationalBankService::reversible($cache);
    $converter = new CurrencyConverter($service);

    // 32.74 as of 2025-11-27
    echo $converter->convert('12500', 'HUF', 'EUR', 2), PHP_EOL;

.. note::
    Reversible Factory emits non-precise services
    that can only be used in informational purposes.
