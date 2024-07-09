using System;
using System.Collections.Generic;

namespace DesignPatterns.Mediator
{
    class CommandCentre
    {
        private List<Runway> _runways = new List<Runway>();
        private List<Aircraft> _aircrafts = new List<Aircraft>();

        public CommandCentre(Runway[] runways, Aircraft[] aircrafts)
        {
            _runways.AddRange(runways);
            _aircrafts.AddRange(aircrafts);
        }

        public void RequestToLand(Aircraft aircraft, Runway runway)
        {
            Console.WriteLine($"Command Centre: Aircraft {aircraft.Name} requests to land on Runway {runway.Id}.");

            if (runway.IsAvailable())
            {
                runway.AssignRunway(aircraft);
                aircraft.Land(runway);
            }
            else
            {
                Console.WriteLine($"Command Centre: Runway {runway.Id} is busy. Aircraft {aircraft.Name} cannot land.");
            }
        }

        public void RequestToTakeOff(Aircraft aircraft, Runway runway)
        {
            Console.WriteLine($"Command Centre: Aircraft {aircraft.Name} requests to take off from Runway {runway.Id}.");

            if (!runway.CheckIsActive())
            {
                Console.WriteLine($"Command Centre: Aircraft {aircraft.Name} can take off from Runway {runway.Id}.");
                aircraft.TakeOff(runway);
            }
            else
            {
                Console.WriteLine($"Command Centre: Runway {runway.Id} is currently active. Aircraft {aircraft.Name} cannot take off.");
            }
        }
    }
}
