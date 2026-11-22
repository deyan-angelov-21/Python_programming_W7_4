from dataclasses import dataclass
DELIMITER = ";"
@dataclass

class TIMESTAMP:
    weekday: str = ""
    hour: str = ""
    consumption: float = 0.0
    price: float = 0.0

def readTimestamps(Filename: str, Timestamps: list[TIMESTAMP]) -> None:
    with open(Filename, "r", encoding="UTF-8") as file:
        for Line in file:
            Row = Line.rstrip()
            if Row == "":
                continue
            Columns = Row.split(DELIMITER)
            if Columns[0].strip().lower() == "weekday":
                continue
            Timestamp = TIMESTAMP()
            Timestamp.weekday = Columns[0]
            Timestamp.hour = Columns[1]
            Timestamp.consumption = float(Columns[2])
            Timestamp.price = float(Columns[3])
            Timestamps.append(Timestamp)
    return None

def displayTimestamps(Timestamps: list[TIMESTAMP]) -> None:
    print("Electricity usages:")
    for Timestamp in Timestamps:
        Total = Timestamp.consumption * Timestamp.price
        print(
            f" - {Timestamp.weekday} {Timestamp.hour}, "
            f"price {Timestamp.price:.2f} €, "
            f"consumption {Timestamp.consumption:.2f} kWh, "
            f"total {Total:.2f} €"
        )
    return None

def main() -> None:
    print("Program starting.")
    Filename = input("Insert filename: ")
    print(f'Reading file "{Filename}".')
    Timestamps: list[TIMESTAMP] = []
    readTimestamps(Filename, Timestamps)
    displayTimestamps(Timestamps)
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()
