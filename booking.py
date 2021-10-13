"""Module name : Booking.py
   Module containing booking related functions"""

import webbrowser     # built-in module


def yatra():
    print("\n\tYATRA")
    place = input("\nEnter Destination : ")
    adults = int(input("Enter total number of Adults : "))
    children = int(input("Enter total number of children : "))
    site1 = "https://www.yatra.com/pwa/hotels/srp?roomRequests[0].id=1&roomRequests[0]."
    site2 = "noOfAdults={}&roomRequests[0].noOfChildren={}&source=BOOKING_ENGINE&"
    site3 = "pg=1&tenant=B2C&isPersnldSrp=1&city.name={}&city.code={}&state.name="
    site4 = "KER&state.code=KER&country.name=India&country.code=IND"
    # Web Address reduced to compensate with Hard copy
    site = site1 + site2 + site3 + site4
    yatra = (site.format(adults, children, place, place))
    print("You are being redirected...")
    webbrowser.open(yatra, new=1)


def easemytrip():
    print("\n\tEASEMYTRIP")
    destination = input("Enter your Destination : ")
    checkin = input("Enter Check-in date in format DD/MM/YYYY : ")
    checkout = input("Enter Check-out date in format DD/MM/YYYY : ")
    pax = input("Enter number of adults : ")
    rooms = input("Enter number of rooms required : ")
    site1 = "https://hotels.easemytrip.com/newhotel/Hotel/HotelListing?e=202193214436&"
    site2 = "city={},%20India&cin={}&cOut={}&Hotel=NA&Rooms={}&pax={}"
    site = site1 + site2         # Web address reduced to compensate with Hard copy
    easemytrip = (site.format(destination, checkin, checkout, rooms, pax))
    print("You are being redirected...")
    webbrowser.open(easemytrip, new=1)
