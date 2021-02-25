select aircrafts.model, count(flights.actual_arrival) as flights_num
from  flights inner join aircrafts on flights.aircraft_code = aircrafts.aircraft_code
group by flights.aircraft_code having flights_num > 0 order by flights_num desc;

select ticket_flights.flight_id, round(avg(ticket_flights.amount)) as avg_amount
from ticket_flights group by ticket_flights.flight_id
having avg_amount > 3300 and avg_amount < 5000
order by ticket_flights.flight_id;

select sum(ticket_flights.amount) as lost_profit
from ticket_flights
where ticket_flights.flight_id in (select flights.flight_id from flights where flights.status = 'Cancelled');

select sum(ticket_flights.amount) as lost_profit
from ticket_flights
where ticket_flights.flight_id in
(select flights.flight_id from flights where flights.status = 'Cancelled' and
(flights.scheduled_departure between '2017-08-17' and '2017-08-23'));

select tmp.dayname, count(tmp.dayname) as flights from
(select dayname(flights.scheduled_departure) as dayname from flights where flights.departure_airport in ('SVO', 'VKO', 'DME')) tmp
group by tmp.dayname order by flights;

select tmp.departure_airport as airport_code, count(ticket_flights.ticket_no) as passengers from
ticket_flights join
(select flights.departure_airport, flights.flight_id from flights
 where flights.departure_airport in ('SVO', 'VKO', 'DME')) tmp on ticket_flights.flight_id = tmp.flight_id
 group by airport_code order by passengers desc;

select tmp.departure_airport as airport_code, count(tmp.departure_airport) as cancelled_flights_number
from (select flights.departure_airport from flights where flights.status = 'Cancelled') tmp
group by airport_code order by cancelled_flights_number desc limit 3;

select tmp.month as month, count(tmp.month) as cancelled_flights_number from
(select month(flights.scheduled_departure) as month from flights where flights.status = 'Cancelled') tmp
group by month order by month;

select airports.city as city, count(airports.city) as cancelled_flights_number from
airports join (select flights.departure_airport from flights where flights.status = 'Cancelled') tmp
on airports.airport_code = tmp.departure_airport
group by city order by cancelled_flights_number desc limit 5;


