import logging
from pathlib import Path

LOG_DIR = Path(__file__).resolve().parent / "logs"
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "application.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
    ],
)

logger = logging.getLogger(__name__)


def calculate_total(price, quantity):
    total = price + quantity
    logger.info("Calculated total: price=%s, quantity=%s, total=%s", price, quantity, total)
    return total


def calculate_discount(total, discount):
    final_amount = total - (total * discount / 100)
    logger.info(
        "Calculated discount: total=%s, discount=%s%%, final_amount=%s",
        total,
        discount,
        final_amount,
    )
    return final_amount


if __name__ == "__main__":
    total = calculate_total(100, 2)
    final_amount = calculate_discount(total, 10)
    print("Total Amount:", total)
    print("Final Amount:", final_amount)
