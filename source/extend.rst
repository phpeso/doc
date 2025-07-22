Write Your Own
##############

.. highlight:: php

Extend Peso in case you need more from it.

Integration
===========

Writing your own integration is easy:

* Depend on ``peso/core``
* Follow the :ref:`core` instruction

Service
=======

To write your own service implementation you need to extend the Service interface::

    <?php

    declare(strict_types=1);

    namespace Peso\Core\Services;

    use Peso\Core\Exceptions\RuntimeException;
    use Peso\Core\Requests\CurrentConversionRequest;
    use Peso\Core\Requests\CurrentExchangeRateRequest;
    use Peso\Core\Requests\HistoricalConversionRequest;
    use Peso\Core\Requests\HistoricalExchangeRateRequest;
    use Peso\Core\Responses\ConversionResponse;
    use Peso\Core\Responses\ErrorResponse;
    use Peso\Core\Responses\ExchangeRateResponse;

    interface PesoServiceInterface
    {
        /**
         * @template T of object
         * @param T $request
         * @return (
         *      T is CurrentExchangeRateRequest ? ExchangeRateResponse|ErrorResponse : (
         *      T is HistoricalExchangeRateRequest ? ExchangeRateResponse|ErrorResponse : (
         *      T is CurrentConversionRequest ? ConversionResponse|ErrorResponse : (
         *      T is HistoricalConversionRequest ? ConversionResponse|ErrorResponse : (
         *      ErrorResponse
         * )))))
         * @throws RuntimeException
         */
        public function send(object $request): ExchangeRateResponse|ConversionResponse|ErrorResponse;

        /**
         */
        public function supports(object $request): bool;
    }

``supports()`` Method
---------------------

The ``supports()`` method is used for a fast check if the service can handle a request.

* If ``supports($request)`` returns false, ``send($request)`` MUST return ``ErrorResponse``.
* ``supports()`` SHOULD NOT do any external requests, it SHOULD be as simple and fast as possible.
* The user is **not** obliged to call ``supports($request)`` before ``send($request)``,
  so ``send($request)`` MUST NOT crash just because it was fed an unsupported request.

``send()`` Method
-----------------

The ``send()`` method executes a request.

* If the request object is not supported, the service MUST return the ``ErrorResponse``.
* The service MUST return a response object that corresponds to the request :ref:`according to the model <model>`.
* The service MAY add custom request objects but not custom response objects.
* You do not need to declare responses in the response type hint that you don't plan to return,
  therefore only the ``ErrorResponse`` is required.
  See PHP manual for Covariance_ and `Union Types`_ in PHP.
* If the request can't be handled for expected and valid reasons, the method MUST return an instance of
  ``ErrorResponse`` that wraps an instance of ``Peso\Core\Exceptions\PesoResponseException``. (MUST NOT throw!)
  For example, if the currency pair or the request type itself is unsupported.
* If the request can't be handled for some unexpected reason, like network failure or unexpected response from a server,
  the method MUST throw either an instance of ``Peso\Core\Exceptions\RuntimeException`` or an instance of ``\Error``.

.. _Covariance: https://www.php.net/manual/en/language.oop5.variance.php
.. _Union Types: https://www.php.net/manual/en/language.types.type-system.php#language.types.type-system.composite.union
