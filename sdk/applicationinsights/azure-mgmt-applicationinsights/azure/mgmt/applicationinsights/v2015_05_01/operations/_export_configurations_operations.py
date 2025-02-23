# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, List, Optional, TypeVar

from msrest import Serializer

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from .._vendor import _convert_request, _format_url_section
T = TypeVar('T')
JSONType = Any
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

def build_list_request(
    resource_group_name: str,
    subscription_id: str,
    resource_name: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = kwargs.pop('api_version', "2015-05-01")  # type: str

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/exportconfiguration")  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str', min_length=1),
        "resourceName": _SERIALIZER.url("resource_name", resource_name, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )


def build_create_request(
    resource_group_name: str,
    subscription_id: str,
    resource_name: str,
    *,
    json: JSONType = None,
    content: Any = None,
    **kwargs: Any
) -> HttpRequest:
    api_version = kwargs.pop('api_version', "2015-05-01")  # type: str
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/exportconfiguration")  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str', min_length=1),
        "resourceName": _SERIALIZER.url("resource_name", resource_name, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        _header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        json=json,
        content=content,
        **kwargs
    )


def build_delete_request(
    resource_group_name: str,
    subscription_id: str,
    resource_name: str,
    export_id: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = kwargs.pop('api_version', "2015-05-01")  # type: str

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/exportconfiguration/{exportId}")  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str', min_length=1),
        "resourceName": _SERIALIZER.url("resource_name", resource_name, 'str'),
        "exportId": _SERIALIZER.url("export_id", export_id, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="DELETE",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )


def build_get_request(
    resource_group_name: str,
    subscription_id: str,
    resource_name: str,
    export_id: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = kwargs.pop('api_version', "2015-05-01")  # type: str

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/exportconfiguration/{exportId}")  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str', min_length=1),
        "resourceName": _SERIALIZER.url("resource_name", resource_name, 'str'),
        "exportId": _SERIALIZER.url("export_id", export_id, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )


def build_update_request(
    resource_group_name: str,
    subscription_id: str,
    resource_name: str,
    export_id: str,
    *,
    json: JSONType = None,
    content: Any = None,
    **kwargs: Any
) -> HttpRequest:
    api_version = kwargs.pop('api_version', "2015-05-01")  # type: str
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/exportconfiguration/{exportId}")  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str', min_length=1),
        "resourceName": _SERIALIZER.url("resource_name", resource_name, 'str'),
        "exportId": _SERIALIZER.url("export_id", export_id, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        _header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        json=json,
        content=content,
        **kwargs
    )

class ExportConfigurationsOperations(object):
    """ExportConfigurationsOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.applicationinsights.v2015_05_01.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def list(
        self,
        resource_group_name: str,
        resource_name: str,
        **kwargs: Any
    ) -> List["_models.ApplicationInsightsComponentExportConfiguration"]:
        """Gets a list of Continuous Export configuration of an Application Insights component.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param resource_name: The name of the Application Insights component resource.
        :type resource_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of ApplicationInsightsComponentExportConfiguration, or the result of
         cls(response)
        :rtype:
         list[~azure.mgmt.applicationinsights.v2015_05_01.models.ApplicationInsightsComponentExportConfiguration]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["_models.ApplicationInsightsComponentExportConfiguration"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2015-05-01")  # type: str

        
        request = build_list_request(
            resource_group_name=resource_group_name,
            subscription_id=self._config.subscription_id,
            resource_name=resource_name,
            api_version=api_version,
            template_url=self.list.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('[ApplicationInsightsComponentExportConfiguration]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/exportconfiguration"}  # type: ignore


    @distributed_trace
    def create(
        self,
        resource_group_name: str,
        resource_name: str,
        export_properties: "_models.ApplicationInsightsComponentExportRequest",
        **kwargs: Any
    ) -> List["_models.ApplicationInsightsComponentExportConfiguration"]:
        """Create a Continuous Export configuration of an Application Insights component.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param resource_name: The name of the Application Insights component resource.
        :type resource_name: str
        :param export_properties: Properties that need to be specified to create a Continuous Export
         configuration of a Application Insights component.
        :type export_properties:
         ~azure.mgmt.applicationinsights.v2015_05_01.models.ApplicationInsightsComponentExportRequest
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of ApplicationInsightsComponentExportConfiguration, or the result of
         cls(response)
        :rtype:
         list[~azure.mgmt.applicationinsights.v2015_05_01.models.ApplicationInsightsComponentExportConfiguration]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["_models.ApplicationInsightsComponentExportConfiguration"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2015-05-01")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(export_properties, 'ApplicationInsightsComponentExportRequest')

        request = build_create_request(
            resource_group_name=resource_group_name,
            subscription_id=self._config.subscription_id,
            resource_name=resource_name,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.create.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('[ApplicationInsightsComponentExportConfiguration]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/exportconfiguration"}  # type: ignore


    @distributed_trace
    def delete(
        self,
        resource_group_name: str,
        resource_name: str,
        export_id: str,
        **kwargs: Any
    ) -> "_models.ApplicationInsightsComponentExportConfiguration":
        """Delete a Continuous Export configuration of an Application Insights component.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param resource_name: The name of the Application Insights component resource.
        :type resource_name: str
        :param export_id: The Continuous Export configuration ID. This is unique within a Application
         Insights component.
        :type export_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ApplicationInsightsComponentExportConfiguration, or the result of cls(response)
        :rtype:
         ~azure.mgmt.applicationinsights.v2015_05_01.models.ApplicationInsightsComponentExportConfiguration
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ApplicationInsightsComponentExportConfiguration"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2015-05-01")  # type: str

        
        request = build_delete_request(
            resource_group_name=resource_group_name,
            subscription_id=self._config.subscription_id,
            resource_name=resource_name,
            export_id=export_id,
            api_version=api_version,
            template_url=self.delete.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ApplicationInsightsComponentExportConfiguration', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    delete.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/exportconfiguration/{exportId}"}  # type: ignore


    @distributed_trace
    def get(
        self,
        resource_group_name: str,
        resource_name: str,
        export_id: str,
        **kwargs: Any
    ) -> "_models.ApplicationInsightsComponentExportConfiguration":
        """Get the Continuous Export configuration for this export id.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param resource_name: The name of the Application Insights component resource.
        :type resource_name: str
        :param export_id: The Continuous Export configuration ID. This is unique within a Application
         Insights component.
        :type export_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ApplicationInsightsComponentExportConfiguration, or the result of cls(response)
        :rtype:
         ~azure.mgmt.applicationinsights.v2015_05_01.models.ApplicationInsightsComponentExportConfiguration
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ApplicationInsightsComponentExportConfiguration"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2015-05-01")  # type: str

        
        request = build_get_request(
            resource_group_name=resource_group_name,
            subscription_id=self._config.subscription_id,
            resource_name=resource_name,
            export_id=export_id,
            api_version=api_version,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ApplicationInsightsComponentExportConfiguration', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/exportconfiguration/{exportId}"}  # type: ignore


    @distributed_trace
    def update(
        self,
        resource_group_name: str,
        resource_name: str,
        export_id: str,
        export_properties: "_models.ApplicationInsightsComponentExportRequest",
        **kwargs: Any
    ) -> "_models.ApplicationInsightsComponentExportConfiguration":
        """Update the Continuous Export configuration for this export id.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param resource_name: The name of the Application Insights component resource.
        :type resource_name: str
        :param export_id: The Continuous Export configuration ID. This is unique within a Application
         Insights component.
        :type export_id: str
        :param export_properties: Properties that need to be specified to update the Continuous Export
         configuration.
        :type export_properties:
         ~azure.mgmt.applicationinsights.v2015_05_01.models.ApplicationInsightsComponentExportRequest
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ApplicationInsightsComponentExportConfiguration, or the result of cls(response)
        :rtype:
         ~azure.mgmt.applicationinsights.v2015_05_01.models.ApplicationInsightsComponentExportConfiguration
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ApplicationInsightsComponentExportConfiguration"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2015-05-01")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(export_properties, 'ApplicationInsightsComponentExportRequest')

        request = build_update_request(
            resource_group_name=resource_group_name,
            subscription_id=self._config.subscription_id,
            resource_name=resource_name,
            export_id=export_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.update.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ApplicationInsightsComponentExportConfiguration', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/exportconfiguration/{exportId}"}  # type: ignore

