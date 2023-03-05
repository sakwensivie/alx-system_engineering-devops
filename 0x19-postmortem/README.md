# Postmortem on the Great Llama Incident of 2023

-----

[]: # Path: 0x19-postmortem/README.md

## Issue Summary

On March 3, 2023, our web application experienced a database connection issue that caused users to experience slow page loads and timeouts. The issue lasted from 2:00 PM to 4:30 PM EST, during which approximately 30% of users were unable to access the application. We'd like to apologize to all affected users and assure them that we're taking steps to prevent similar issues from occurring in the future.

## Timeline

1. 2:00 PM: The issue was first detected when our monitoring system started freaking out, sending us so many alerts that we thought we'd accidentally left it on "spaz mode."
2. 2:05 PM: Our engineers began frantically investigating the issue, but their initial theories were all over the place. One engineer even suggested that the database had been hijacked by a pack of rogue llamas.
3. 2:20 PM: We attempted to restart the database server, hoping that it would resolve the issue. It didn't, but we did all learn a valuable lesson about the limits of the "turn it off and on again" approach.
4. 2:35 PM: As we struggled to make sense of the situation, we were all struck by a sudden, inexplicable craving for cheeseburgers.
5. 3:15 PM: We finally identified the real issue: a misconfigured network setting that was preventing the application server from connecting to the database server. It was a classic case of "whoops, my bad."
6. 3:30 PM: We fixed the network configuration and confirmed that the application server was able to connect to the database server once again. There were high-fives all around, and we all agreed that we should probably order some celebratory cheeseburgers.
7. 4:30 PM: The issue was officially resolved, and we were all free to go home and recover from the stress of the afternoon.

-----

## Root Cause and Resolution

The root cause of the issue was a simple misconfiguration of a network setting. Unfortunately, it took us a while to figure that out because we were too busy chasing down wild llama theories and thinking about cheeseburgers. Once we did identify the issue, we were able to fix it quickly by correcting the network configuration setting.

## Corrective and Preventative Measures

To prevent similar issues from occurring in the future, we've implemented the following measures:

We've reviewed all network configuration settings to ensure that they're correct and optimized. We've also promised to stop making changes after "just one more tweak."
We've added additional monitoring to provide early detection of database connection issues, because we're not going to let those sneaky llamas catch us off guard again.
We've developed and implemented a plan for quickly addressing database connection issues, including clear escalation procedures and response time targets. We've also started a company-wide campaign to remind everyone that it's always a good idea to double-check your work.
We've added a new "cheeseburger" tag to our issue tracking system, so that we can easily identify and prioritize issues that are related to cheeseburgers.

## Tasks to address the issue include

Thoroughly researching any llama-related database issues that may arise in the future.
Conducting a full review of all other animal-related threats to our system, just in case.
Planning a company picnic where we all eat cheeseburgers and bond over the trauma of the great llama incident of 2023.
We hope this post-mortem has provided some valuable insights into our recent outage, and that you've enjoyed our attempts at humor. We take all issues seriously and are always striving to improve our systems to better serve our users.
