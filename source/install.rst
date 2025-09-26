Installation
############

To install Peso, first select the desired integration lib, then the desired service lib, like so:

.. code-block:: bash

    composer require peso/peso peso/ecb-service php-http/discovery guzzlehttp/guzzle symfony/cache

In this example

* ``peso/peso`` is a simple wrapper over Peso services for standalone use
* ``peso/ecb-service`` is a service provider for the European Central Bank
* ECB service dependencies, same for all HTTP integrations:

  * ``php-http/discovery`` is a HTTP client autoconfigure package.
    It is not required, you can configure the client manually.
  * ``guzzlehttp/guzzle`` is a HTTP client known to ``php-http/discovery``.
    Any client supporting PSR-18 would do.
  * ``symfony/cache`` is a cache library if you need caching.
    Any PSR-16 library would do. (recommended)

.. list-table:: Available integrations:

    * * ``peso/peso``
      * .. image:: https://img.shields.io/packagist/v/peso/peso.svg?style=flat-square
           :target: https://packagist.org/packages/peso/peso
      * :ref:`A simple standalone currency converter <peso_peso>`
    * * ``peso/moneyphp-exchange``
      * .. image:: https://img.shields.io/packagist/v/peso/moneyphp-exchange.svg?style=flat-square
           :target: https://packagist.org/packages/peso/moneyphp-exchange
      * :ref:`Exchange classes for the Money for PHP library <peso_moneyphp>`
    * * ``peso/brick-rateprovider``
      * .. image:: https://img.shields.io/packagist/v/peso/brick-rateprovider.svg?style=flat-square
           :target: https://packagist.org/packages/peso/brick-rateprovider
      * :ref:`RateProvider classes for the Brick\\Money library <peso_brick>`

.. list-table:: Available services:

    * * ``peso/ecb-service``
      * .. image:: https://img.shields.io/packagist/v/peso/ecb-service.svg?style=flat-square
           :target: https://packagist.org/packages/peso/ecb-service
      * :ref:`ecb_service`
    * * ``peso/cnb-service``
      * .. image:: https://img.shields.io/packagist/v/peso/cnb-service.svg?style=flat-square
           :target: https://packagist.org/packages/peso/cnb-service
      * :ref:`cnb_service`
    * * ``peso/bnr-service``
      * .. image:: https://img.shields.io/packagist/v/peso/bnr-service.svg?style=flat-square
           :target: https://packagist.org/packages/peso/bnr-service
      * :ref:`bnr_service`
    * * ``peso/fixer-service``
      * .. image:: https://img.shields.io/packagist/v/peso/fixer-service.svg?style=flat-square
           :target: https://packagist.org/packages/peso/fixer-service
      * :ref:`fixer_service`
    * * ``peso/openexchangerates-service``
      * .. image:: https://img.shields.io/packagist/v/peso/openexchangerates-service.svg?style=flat-square
           :target: https://packagist.org/packages/peso/openexchangerates-service
      * :ref:`openexchangerates_service`
    * * ``peso/freecurrencyapi-service``
      * .. image:: https://img.shields.io/packagist/v/peso/freecurrencyapi-service.svg?style=flat-square
           :target: https://packagist.org/packages/peso/freecurrencyapi-service
      * :ref:`freecurrencyapi_service`
    * * ``peso/currencyapi-service``
      * .. image:: https://img.shields.io/packagist/v/peso/currencyapi-service.svg?style=flat-square
           :target: https://packagist.org/packages/peso/currencyapi-service
      * :ref:`currencyapi_service`

.. list-table:: Available interoperability connectors:

    * * ``peso/peso-exchanger-interop``
      * .. image:: https://img.shields.io/packagist/v/peso/peso-exchanger-interop.svg?style=flat-square
           :target: https://packagist.org/packages/peso/peso-exchanger-interop
      * :ref:`Exchanger and Swap <exchanger_interop>`
