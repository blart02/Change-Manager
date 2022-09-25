Welcome to the Concern Change Management tool; a tool designed to compliment my organisation's change management processes.

It is built on the Django framework, version 4.1.1.

The application consists of one main project, named 'changemanager', and one custom app named 'main.'

The custom app (main), has 4 models - Requestor, representing a person in the business; Service, representing services that we operate (and requestors work for) and receive requests from;
Change Request, representing a specific change request, logged against a Requestor; finally, Change Request Updates are used by users to log updates to the change request.
An entity relationship diagram representing these relationships is avaliable in the main 

Standard users and Admin users both have access to the main web application, with standard users being unable to access the deletion function. Additionally, admin users have access to an 'admin' area,
where changes to user accounts and the application's underlying data can be made. The user registration form creates standard users by default, to access admin features, please use the login details below.

Admin Login details: (Needed to access the admin functions of the app)
Username - admin
Password - P@ssword1!

