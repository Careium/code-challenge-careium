Backend coding challenge
========================

![](https://images.unsplash.com/photo-1518558406542-3dc7f0e69a40?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=3750&q=80)

Traffic was a nightmare
-----------------------

Is there anything more annoying than getting stuck in traffic? Even if you can pull up Google Maps and check the traffic situation the sad reality is that the times you get stuck in traffic your forgot to check.

The challenge is to create a service to help with this, and to create a simple app UI that uses this service.
This service will use a public traffic incident system as source for sending updates to geo-located connected clients.
We want a REST or graphQL API for the alert service.

Think about scoping and time. Don't overspend your time.

Feel free to use 3rd party providers for SMS, email etc. Twilio is a popular one

Coding Challenge
----------------

# Requirements

- [ ] We want to pull data from the [ Sveriges Radion Trafik API](https://sverigesradio.se/api/documentation/v2/metoder/trafik.html)
- [ ] A client must provide a geolocation for traffic notifications
- [ ] A client can update the geolocation for traffic notifications
- [ ] A client shows a relevant traffic incident that contains at a minimum
  - [ ] Priority
  - [ ] Title
  - [ ] Location
  - [ ] Description
  - [ ] Category

# Bonus if you include
- [ ] A client can register and receive update alerts using email or SMS (phone mumber) as identifier 
- [ ] A registred client will automatically unregister after 24 hours (to be polite)
- [ ] A registred client can unsubscribe from the service

# Tech requirements

- React for the frontend
- CSSinJS is a plus, but not a requirement (JSS, styled-components)
- Python, Java or node.js are good alternatives for the backend
- Tests (appropriate tests to the solution chosen)
- Linter (of your choice)

# Instructions

- Fork this repo, or if you don't want to fork, make your own private and invite us
- Build a clean and robust solution 
- Publish on your chosen cloud provider
- Let us know that you've completed the challenge

# Extra

Before we talk:
- Do surprise us, we love it
- Guide us through what you did; in commits or other way
- So we like you (probably since you did the challenge): But what stands out, why you?


When we talk
------------

We expect you talk talk about

* Description of solution.
* Whether the solution focuses on back-end, front-end or if it's full stack.
* Reasoning behind your technical choices, including architectural. 
* Trade-offs you might have made, anything you left out, or what you might do differently if you were to spend additional time on the project.
* Link to to the hosted application where applicable.

How we review
-------------

Your application will be reviewed by our engineers. We do take into consideration your experience level.

* **Architecture**: how clean is the separation between the front-end and the back-end?
* **Clarity**: does the README clearly and concisely explains the problem and solution? Are technical tradeoffs explained?
* **Correctness**: does the application do what was asked? If there is anything missing, does the README explain why it is missing?
* **Code quality**: is the code simple, easy to understand, and maintainable?  Are there any code smells or other red flags? Does object-oriented code follows principles such as the single responsibility principle? Is the coding style consistent with the language's guidelines? Is it consistent throughout the codebase?
* **Security**: are there any obvious vulnerability?
* **Testing**: how thorough are the automated tests? Will they be difficult to change if the requirements of the application were to change? Are there some unit and some integration tests?
	* We're not looking for full coverage (given time constraint) but just trying to get a feel for your testing skills.
* **UX**: is the web interface understandable and pleasing to use? Is the API intuitive?
* **Technical choices**: do choices of libraries, databases, architecture etc. seem appropriate for the chosen application?

Bonus point (those items are optional):

* **Scalability**: will technical choices scale well? If not, is there a discussion of those choices in the README? 
* **Production-readiness**: does the code include monitoring? logging? proper error handling?



# License

This project is licensed under MIT. Feel free to use it anyway you see fit.

