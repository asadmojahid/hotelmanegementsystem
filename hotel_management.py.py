class Hotel:
    def __init__(self):
        self.rooms = {
            101: {'type': 'Single', 'price': 2000, 'status': 'Available', 'customer': None},
            102: {'type': 'Single', 'price': 2000, 'status': 'Available', 'customer': None},
            103: {'type': 'Double', 'price': 3500, 'status': 'Available', 'customer': None},
            104: {'type': 'Double', 'price': 3500, 'status': 'Available', 'customer': None},
            201: {'type': 'Suite', 'price': 5000, 'status': 'Available', 'customer': None},
            202: {'type': 'Suite', 'price': 5000, 'status': 'Available', 'customer': None}
        }
        self.customers = {}
        self.booking_id = 1

    def display_rooms(self):
        print("\n" + "="*70)
        print("           📋 AVAILABLE ROOMS STATUS")
        print("="*70)
        print(f"{'Room No':<8} {'Type':<10} {'Price':<8} {'Status':<12} {'Customer':<15}")
        print("-"*70)
        for room, details in self.rooms.items():
            customer_name = details['customer'] if details['customer'] else "None"
            print(f"{room:<8} {details['type']:<10} ₹{details['price']:<8} {details['status']:<12} {customer_name:<15}")

    def book_room(self):
        print("\n" + "="*35)
        print("           🏠 BOOK ROOM")
        print("="*35)
        
        name = input("👤 Enter customer name: ").strip()
        phone = input("📱 Enter phone number: ").strip()
        
        try:
            room_no = int(input("🔢 Enter room number to book: "))
        except ValueError:
            print("❌ Please enter valid room number!")
            return
        
        if room_no not in self.rooms:
            print("❌ Invalid room number! Check room list first.")
            return
            
        if self.rooms[room_no]['status'] == 'Booked':
            current_customer = self.rooms[room_no]['customer']
            print(f"❌ Room {room_no} is ALREADY BOOKED by '{current_customer}'!")
            print("💡 Please checkout first or choose another room.")
            return
            
        self.rooms[room_no]['status'] = 'Booked'
        self.rooms[room_no]['customer'] = name
        
        booking_details = {
            'name': name,
            'phone': phone,
            'room': room_no,
            'price': self.rooms[room_no]['price']
        }
        self.customers[self.booking_id] = booking_details
        
        print(f"\n🎉 Room {room_no} booked SUCCESSFULLY for {name}!")
        print(f"💰 Total Amount: ₹{self.rooms[room_no]['price']}")
        print(f"📞 Contact: {phone}")
        print(f"🆔 Booking ID: {self.booking_id}")
        
        self.booking_id += 1

    def check_out(self):
        print("\n" + "="*35)
        print("           🚪 CHECK OUT")
        print("="*35)
        
        try:
            room_no = int(input("🔢 Enter room number to checkout: "))
        except ValueError:
            print("❌ Please enter valid room number!")
            return
        
        if room_no not in self.rooms:
            print("❌ Invalid room number!")
            return
            
        if self.rooms[room_no]['status'] == 'Booked':
            customer_name = self.rooms[room_no]['customer']
            print(f"\n✅ Checkout SUCCESSFUL for {customer_name}")
            print(f"🆓 Room {room_no} is now AVAILABLE")
            
            for bid, details in list(self.customers.items()):
                if details['room'] == room_no:
                    del self.customers[bid]
                    break
                    
            self.rooms[room_no]['status'] = 'Available'
            self.rooms[room_no]['customer'] = None
        else:
            print(f"❌ Room {room_no} is not booked!")

    def view_bookings(self):
        print("\n" + "="*70)
        print("           📋 CURRENT BOOKINGS")
        print("="*70)
        print(f"{'ID':<5} {'Name':<15} {'Room':<8} {'Phone':<12} {'Price':<10}")
        print("-"*70)
        
        if not self.customers:
            print("📭 No current bookings!")
            return
        
        for bid, details in self.customers.items():
            print(f"{bid:<5} {details['name']:<15} {details['room']:<8} "
                  f"{details['phone']:<12} ₹{details['price']:<10}")

def main():
    hotel = Hotel()
    
    while True:
        print("\n" + "="*55)
        print("      🏨 HOTEL MANAGEMENT SYSTEM 🏨")
        print("="*55)
        print("1. 📋 View All Rooms")
        print("2. 🏠 Book Room")
        print("3. 🚪 Checkout")
        print("4. 📋 View Bookings")
        print("5. ❌ Exit")
        print("-"*55)
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            hotel.display_rooms()
        elif choice == '2':
            hotel.book_room()
        elif choice == '3':
            hotel.check_out()
        elif choice == '4':
            hotel.view_bookings()
        elif choice == '5':
            print("\n👋 Thank you for using Hotel Management System!")
            break
        else:
            print("❌ Invalid choice! Enter 1-5 only.")

if __name__ == "__main__":
    main()