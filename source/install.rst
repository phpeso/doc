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
  * ``symfony/cache`` a cache library if you need caching. (recommended)

Available integrations:

.. list-table::

    * * ``peso/peso``
      * .. image:: https://img.shields.io/packagist/v/peso/peso.svg?style=flat-square
           :target: https://packagist.org/packages/peso/peso
      * :ref:`A simple standalone currency converter <peso_peso>`
    * * ``peso/moneyphp-exchange``
      * .. image:: https://img.shields.io/packagist/v/peso/moneyphp-exchange.svg?style=flat-square
           :target: https://packagist.org/packages/peso/moneyphp-exchange
      * :ref:`Exchange class for the Money for PHP library <peso_moneyphp>`

Available services:

.. list-table::

    * * ``peso/ecb-service``
      * .. image:: https://img.shields.io/packagist/v/peso/ecb-service.svg?style=flat-square
           :target: https://packagist.org/packages/peso/ecb-service
      * :ref:`European Central Bank <ecb_service>`
    * * ``peso/cnb-service``
      * .. image:: https://img.shields.io/packagist/v/peso/cnb-service.svg?style=flat-square
           :target: https://packagist.org/packages/peso/cnb-service
      * :ref:`Czech National Bank <cnb_service>`
    * * ``peso/fixer-service``
      * .. image:: https://img.shields.io/packagist/v/peso/fixer-service.svg?style=flat-square
           :target: https://packagist.org/packages/peso/fixer-service
      * :ref:`Fixer <fixer_service>`
    * * ``peso/openexchangerates-service``
      * .. image:: https://img.shields.io/packagist/v/peso/openexchangerates-service.svg?style=flat-square
           :target: https://packagist.org/packages/peso/openexchangerates-service
      * :ref:`Open Exchange Rates <openexchangerates_service>`

Available interoperability connectors:

.. list-table::

    * * ``peso/peso-exchanger-interop``
      * .. image:: https://img.shields.io/packagist/v/peso/peso-exchanger-interop.svg?style=flat-square
           :target: https://packagist.org/packages/peso/peso-exchanger-interop
      * :ref:`Exchanger and Swap <exchanger_interop>`
