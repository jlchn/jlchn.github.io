
---
layout: default
title: Buttons
parent: Spring Framework
nav_order: 1
---

### @EnableAutoConfiguration

@EnableAutoConfiguration tells Spring Boot to configure Spring based on the libaray dependencies 

If spring-boot-starter-web is in the dependency and thus added Tomcat and Spring MVC added, the EnableAutoConfiguration will assume that we are developing a web application and setup Spring accordingly.

> by adding spring-boot-starter-web to our projects, we can simply run  `mvn spring-boot:run` from the root project directory to start our application

### @Comfiguration
 
 a class with the @Configuration indicates that this class will be used by JavaConfig as a source of bean definitions.
