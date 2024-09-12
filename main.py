from src.com.abnamro.transactionanalysis.constants import Constants
from src.com.abnamro.transactionanalysis.service.AccountOverviewService import AccountOverviewService

if __name__ == "__main__":
    # Database configuration for PostgreSQL
    db_config = {
        'host': Constants.HOST,
        'port': Constants.PORT,
        'dbname': Constants.DATABASE_NAME,
        'user': Constants.USER_NAME,
        'password': Constants.PASSWORD
    }

    # Initialize the account overview service
    account_service = AccountOverviewService(db_config)

    # Connect to the database
    account_service.connect()

    # Path to the CSV file
    csv_file_path = Constants.CSV_FILE_PATH

    # Insert records from the CSV file into the account_overview table
    account_service.insert_from_csv(csv_file_path)

    # Close the connection to the database
    account_service.close_connection()
