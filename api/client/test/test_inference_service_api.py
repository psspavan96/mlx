# Copyright 2021 IBM Corporation
# 
# Licensed under the Apache License, Version 2.0 (the "License"); 
# you may not use this file except in compliance with the License. 
# You may obtain a copy of the License at 
# 
#     http://www.apache.org/licenses/LICENSE-2.0 
# 
# Unless required by applicable law or agreed to in writing, software 
# distributed under the License is distributed on an "AS IS" BASIS, 
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
# See the License for the specific language governing permissions and 
# limitations under the License. 
# coding: utf-8

"""
    MLX API

    MLX API Extension for Kubeflow Pipelines  # noqa: E501

    OpenAPI spec version: 0.1.27-pipeline-namespace
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.inference_service_api import InferenceServiceApi  # noqa: E501
from swagger_client.rest import ApiException


class TestInferenceServiceApi(unittest.TestCase):
    """InferenceServiceApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.inference_service_api.InferenceServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_service(self):
        """Test case for get_service

        """
        pass

    def test_list_services(self):
        """Test case for list_services

        Gets all KFServing services  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
