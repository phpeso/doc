Installation
############

To install Peso, first select the desired integration lib, then the desired service lib, like so:

.. code-block:: bash

    composer install peso/peso peso/ecb-service php-http/discovery guzzlehttp/guzzle symfony/cache

In this example

* ``peso/peso`` is a simple frontend that acts like an integration lib
* ``peso/ecb-service`` is a service provider for the European Central Bank
* ECB service dependencies, same for all HTTP integrations:

  * ``php-http/discovery`` is a HTTP client autoconfigure package.
    It is not required, you can configure the client manually.
  * ``guzzlehttp/guzzle`` is a HTTP client known to ``php-http/discovery``.
    Any client supporting PSR-18 would do.
  * ``symfony/cache`` a cache library if you need caching. (recommended)

Version notes:

* Alpha series: 0.1.x, ... 0.8.x—Unstable to use
* Beta series: 0.9.x, 0.10.x, ...—Stable to use but interfaces may rapidly change
* Release series: 1.x—Expected in July or August 2025

Available integrations:

.. list-table::

    * * ``peso/peso``
      * :ref:`A simple frontend <peso_peso>`
    * * ``peso/moneyphp-exchange``
      * :ref:`Exchange class for the Money for PHP library <peso_moneyphp>`

Available services:

.. list-table::

    * * ``peso/ecb-service``
      * :ref:`European Central Bank <ecb_service>`
    * * ``peso/cnb-service``
      * :ref:`Czech National Bank <cnb_service>`
    * * ``peso/fixer-service``
      * :ref:`Fixer <fixer_service>`
    * * ``peso/openexchangerates-service``
      * :ref:`Open Exchange Rates <openexchangerates_service>`
