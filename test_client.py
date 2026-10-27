
from zeep import Client
from zeep.exceptions import Fault, TransportError
import time

# SOAP service configuration
WSDL_URL = "http://127.0.0.1:8000/?wsdl"

# Test counters
total_tests = 0
passed_tests = 0
failed_tests = 0


def print_header(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def run_test(test_name, operation):
    global total_tests, passed_tests, failed_tests

    total_tests += 1
    print(f"\nTest {total_tests}: {test_name}")

    try:
        start_time = time.time()
        result = operation()
        elapsed = (time.time() - start_time) * 1000

        print(f"Response : {result}")
        print(f"Time     : {elapsed:.2f} ms")

        if result is not None and str(result).strip():
            print("Status   : PASS")
            passed_tests += 1
        else:
            print("Status   : FAIL - Empty response")
            failed_tests += 1

    except (Fault, TransportError, Exception) as error:
        print(f"Error    : {error}")
        print("Status   : FAIL")
        failed_tests += 1


def main():
    print_header("STUDENT INFORMATION SOAP SERVICE - CLIENT TESTING")

    print("Connecting to SOAP service...")
    print(f"WSDL URL: {WSDL_URL}")

    try:
        client = Client(wsdl=WSDL_URL)
        print("Connection Status: SUCCESS")
    except Exception as error:
        print("Connection Status: FAILED")
        print(f"Reason: {error}")
        print("\nMake sure student_service.py is running.")
        return

    # Test 1: Retrieve a valid student's name
    run_test(
        "Retrieve student name - ID 101",
        lambda: client.service.get_student_name(101)
    )

    # Test 2: Retrieve another student's name
    run_test(
        "Retrieve student name - ID 102",
        lambda: client.service.get_student_name(102)
    )

    # Test 3: Retrieve complete student details
    run_test(
        "Retrieve complete details - ID 101",
        lambda: client.service.get_student(101)
    )

    # Test 4: Retrieve details for another student
    run_test(
        "Retrieve complete details - ID 103",
        lambda: client.service.get_student(103)
    )

    # Test 5: Check an invalid student ID
    run_test(
        "Handle invalid student ID - ID 999",
        lambda: client.service.get_student(999)
    )

    # Test 6: Check an invalid ID using the name operation
    run_test(
        "Handle invalid name request - ID 999",
        lambda: client.service.get_student_name(999)
    )

    # Test 7: Check the service response type
    run_test(
        "Verify response type for student name",
        lambda: (
            client.service.get_student_name(101)
            if isinstance(client.service.get_student_name(101), str)
            else ""
        )
    )

    # Final summary
    print_header("TEST EXECUTION SUMMARY")
    print(f"Total Tests : {total_tests}")
    print(f"Passed      : {passed_tests}")
    print(f"Failed      : {failed_tests}")

    if failed_tests == 0:
        print("\nOverall Result: ALL TESTS PASSED")
    else:
        print("\nOverall Result: SOME TESTS FAILED")

    print("=" * 60)


if __name__ == "__main__":
    main()
