def test_health_check(api_client, result_logger):
    response = api_client.get("health")
    assert response.status_code == 200
    result_logger.log_result("Health Check", "passed" if response.status_code == 200 else "failed", "dev")
