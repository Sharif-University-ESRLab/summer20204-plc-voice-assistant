from pymodbus.client import ModbusTcpClient
from pymodbus.exceptions import ModbusIOException
from pymodbus.pdu import ExceptionResponse

def connect_to_plc(ip, port):
    client = ModbusTcpClient(ip, port=port)
    if client.connect():
        print("Connected to PLC")
    else:
        print("Failed to connect to PLC")
    return client

def read_register(client, address):
    try:
        response = client.read_holding_registers(address, 1)
        if isinstance(response, ExceptionResponse):
            print(f"Modbus exception: {response}")
            return None
        if not response.isError():
            return response.registers[0]
        else:
            print(f"Error reading register at address {address}: {response}")
            return None
    except ModbusIOException as e:
        print(f"IO error reading register: {e}")
        return None

def write_register(client, address, value):
    try:
        response = client.write_register(address, value)
        if isinstance(response, ExceptionResponse):
            print(f"Modbus exception: {response}")
            return None
        if not response.isError():
            print(f"Successfully wrote {value} to register at address {address}")
        else:
            print(f"Error writing to register at address {address}: {response}")
    except ModbusIOException as e:
        print(f"IO error writing to register: {e}")

def main():
    ip = "192.168.1.17"  # Replace with your PLC's IP address
    port = 139  # Modbus TCP port

    client = connect_to_plc(ip, port)
    if client:
        # Replace with actual register addresses
        register_on = 0  # Example address for "turn_on_light"
        register_off = 1  # Example address for "turn_off_light"

        # Write to registers
        write_register(client, register_on, 1)  # Turn on light (value = 1)
        write_register(client, register_off, 0)  # Turn off light (value = 0)

        # Read back to verify
        current_status_on = read_register(client, register_on)
        print(f"Turn on light register value: {current_status_on}")

        current_status_off = read_register(client, register_off)
        print(f"Turn off light register value: {current_status_off}")

        client.close()

if name == "__main__":
    main
