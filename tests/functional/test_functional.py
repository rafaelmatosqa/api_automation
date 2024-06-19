def test_functional(api_client, result_logger):
    response = api_client.post("some_endpoint", data={"key": "value"})
    assert response.status_code == 201
    result_logger.log_result("Functional Test", "passed" if response.status_code == 201 else "failed", "dev")
