# Coding challenge

![](https://images.unsplash.com/photo-1518558406542-3dc7f0e69a40?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=3750&q=80)

## Traffic was a nightmare

Is there anything more annoying than getting stuck in traffic? Even if you can pull up Google Maps and check the traffic situation the sad reality is that the times you get stuck in traffic your forgot to check.

The challenge is to create a service to help with this, and to create a simple app UI that uses this service.
This service will use a public traffic incident system as source for sending updates to geo-located connected clients.
We want a REST or graphQL API for the alert service.

Think about scoping and time. Don't overspend your time.

Feel free to use 3rd party providers.

## Coding Challenge

# Requirements

- [ ] We want to pull data from the [ Sveriges Radio Trafik API](https://sverigesradio.se/api/documentation/v2/metoder/trafik.html)
- [ ] A client must provide a geolocation for traffic notifications
- [ ] A client can update the geolocation for traffic notifications
- [ ] A client shows a relevant traffic incident that contains at a minimum
  - [ ] Priority
  - [ ] Title
  - [ ] Location
  - [ ] Description
  - [ ] Category

# Bonus if you include

- [ ] A client can register and receive updates
- [ ] A registered client will automatically unregister after 24 hours (to be polite)
- [ ] A registered client can unsubscribe from the service

# Tech requirements

This is what we like but if you feel do use other tools feel free, as long as you can explain why.

- React native if you want to show your native skills
- React for the frontend
- Typescript
- Tests (appropriate tests to the solution chosen)
- Linter (of your choice)
- CI/CD if you want to show your devops skill

# Instructions

- Fork this repo, or if you don't want to fork, make your own private and invite us
- Build a clean and robust solution
- Publish on your chosen cloud provider
- Let us know that you've completed the challenge
- Guide us through what you did; in commits or other way
- Do surprise us, we love it

## If this leads to an interview...

We expect you talk about

- Description of solution.
- Reasoning behind your technical choices, including architectural.

## How we review

Your application will be reviewed by our engineers. We do take into consideration your experience level.

When reviewing we look at things like architecture, how easy the code is to understand, deployment readiness, how well it executes the task and more. Think about it as a delivery to a customer.

# License

This project is licensed under MIT. Feel free to use it anyway you see fit.
