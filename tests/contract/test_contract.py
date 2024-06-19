def test_contract(api_client, result_logger):
    response = api_client.get("some_endpoint")
    assert response.status_code == 200
    assert "expected_key" in response.json()
    result_logger.log_result("Contract Test", "passed" if response.status_code == 200 else "failed", "dev")
