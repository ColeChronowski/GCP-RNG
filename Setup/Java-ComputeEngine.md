# Java Compute Engine

Begin by going to cloud.google.com and setting up a project. To set up the instance, begin by clicking compute engine and then "create instance".

When setting up the instance, you will choose which region and zone your instance will run in.
Here, we chose northamerica-northeast1 region and zone a.

![](https://github.com/ColeChronowski/GCP-RNG/raw/master/Setup/images/Screenshot%20(19).png "screenshot")

![](https://github.com/ColeChronowski/GCP-RNG/raw/master/Setup/images/Screenshot%20(20).png "screenshot")

Next, the machine type should be chosen. For our instance, we wanted to use the least expensive type, f1-micro.

![](https://github.com/ColeChronowski/GCP-RNG/raw/master/Setup/images/Screenshot%20(21).png "screenshot")

Next, the boot disk needs to be configured to run Ubuntu 18.04 LTS.

![](https://github.com/ColeChronowski/GCP-RNG/raw/master/Setup/images/Screenshot%20(22).png "screenshot")

Check both boxes to allow HTTP and HTTPS traffic.

![](https://github.com/ColeChronowski/GCP-RNG/raw/master/Setup/images/Screenshot%20(23).png "screenshot")

The next step is to change the firewall rules of the instance. Here, the system needs to allow tcp:80,8080.
To do this, click on the name of the firewall rule and edit the protocol to allow tcp:80,8080.

![](https://github.com/ColeChronowski/GCP-RNG/raw/master/Setup/images/Screenshot%20(29).png "screenshot")

![](https://github.com/ColeChronowski/GCP-RNG/raw/master/Setup/images/Screenshot%20(30).png "screenshot")

![](https://github.com/ColeChronowski/GCP-RNG/raw/master/Setup/images/Screenshot%20(31).png "screenshot")

![](https://github.com/ColeChronowski/GCP-RNG/raw/master/Setup/images/Screenshot%20(32).png "screenshot")

![](https://github.com/ColeChronowski/GCP-RNG/raw/master/Setup/images/Screenshot%20(33).png "screenshot")

Next, open the instance in another window. Here, a few commands need to be run to ensure your instance is up-to-date.

![](https://github.com/ColeChronowski/GCP-RNG/raw/master/Setup/images/Screenshot%20(24).png "screenshot")

![](https://github.com/ColeChronowski/GCP-RNG/raw/master/Setup/images/Screenshot%20(25).png "screenshot")

![](https://github.com/ColeChronowski/GCP-RNG/raw/master/Setup/images/Screenshot%20(26).png "screenshot")

Next, clone the github repository that contains the random number generated code for Java Compute Engine.

![](https://github.com/ColeChronowski/GCP-RNG/raw/master/Setup/images/Screenshot%20(27).png "screenshot")

Change the directory of your instance to the one that contains the Java Compute Engine code.

![](https://github.com/ColeChronowski/GCP-RNG/raw/master/Setup/images/Screenshot%20(28).png "screenshot")

Run the code by typing 
    java -jar start.jar

![](https://github.com/ColeChronowski/GCP-RNG/raw/master/Setup/images/Screenshot%20(36).png "screenshot")

In your browser, copy the external IP address of your instance and go to http://[external IP]:8080/rng.

![](https://github.com/ColeChronowski/GCP-RNG/raw/master/Setup/images/Screenshot%20(35).png "screenshot")

This address shows the output of the random number generator.

![](https://github.com/ColeChronowski/GCP-RNG/raw/master/Setup/images/Screenshot%20(34).png "screenshot")