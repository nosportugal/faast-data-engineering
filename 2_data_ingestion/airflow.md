# More Airflow!

[<img src="../images/2022-09-02-12-55-27.png" align="right">](https://airflow.apache.org/)

This week's lesson covered the basics of Airflow, but there's way more to learn!

In this document, you will find a list of resources that will help you expand your knowledge of Airflow.

Everything's optional, of course. The idea is not for you to read everything right away, but to have a list of references that you can use to when you need to.

## Start here

### Introductions and tutorials

- [Introduction to Airflow](https://www.youtube.com/playlist?list=PLzKRcZrsJN_xcKKyKn18K7sWu5TTtdywh) - A web tutorial series by [maxcotec](https://maxcotec.com) for beginners and intermediate users of Apache Airflow.
- [Testing and debugging Apache Airflow](https://blog.godatadriven.com/testing-and-debugging-apache-airflow) - Article explaining how to apply unit testing, mocking and debugging to Airflow code.
- [Get started with Airflow + Google Cloud Platform + Docker](https://medium.com/@junjiejiang94/get-started-with-airflow-google-cloud-platform-docker-a21c46e0f797) - Step-by-step introduction by [Jayce Jiang](https://medium.com/@junjiejiang94).
- [How to develop data pipeline in Airflow through TDD (test-driven development)](https://blog.magrathealabs.com/how-to-develop-data-pipeline-in-airflow-through-tdd-test-driven-development-c3333439f358) - Learn how to build a sales data pipeline using TDD step-by-step and in the end how to configure a simple CI workflow using GitHub Actions.
- [Puckel's Docker Image](https://github.com/puckel/docker-airflow) - [@Puckel_](https://twitter.com/Puckel_)'s well-crafted Docker image has become the base for many Airflow installations.  It is regularly updated and closely tracks the official Apache releases.

### dbt + Airflow

- [How Airflow + dbt Work Together](https://www.getdbt.com/blog/dbt-airflow/) - FAQs for how to pair dbt with Airflow.
- [The Spiritual Alignment of dbt + Airflow](https://docs.getdbt.com/blog/dbt-airflow-spiritual-alignment) - This post hones in on a couple cases where they play nicely, and then dive into the nitty gritty of which combination of Airflow + dbt might be right for your team.

## Airflow Summit 2020 videos

*The first [Airflow Summit 2020](https://airflowsummit.org/) was held in July 2020. This is a selection of some of their talks*

- [Keynote: How large companies use Airflow for ML and ETL pipelines](https://youtu.be/428AiCBMZoQ)
- [Data DAGs with lineage for fun and for profit](https://youtu.be/l_vVxOdvujg)
- [Data flow with Airflow @ PayPal](https://youtu.be/kAtaj_s4f-w)
- [Run Airflow DAGs in a secure way](https://youtu.be/QhnItssm4yU)
- [Effective Cross-DAG dependency](https://youtu.be/p66GcO0LbFQ)
- [Building reusable and trustworthy ELT pipelines (A templated approach)](https://youtu.be/R4bp3_VyJ70)
- [Pipelines on pipelines: Agile CI/CD workflows for Airflow DAGs](https://youtu.be/tY4F9X5l6dg)

## Best practices, lessons learned and cool use cases

- [Airflow best practices - Reducing DAG complexity](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html#reducing-dag-complexity) - A list of best practices for using Airflow from the maintainer's perspective.
- [Airflow DAG Python Package Management](https://www.youtube.com/watch?v=9pykChPp-X4&t=121s) - Managing python package dependencies across 100+ DAGs can become painful. It's hard to keep track of which packages are used by which DAG, and hard to clean up during DAG removal/upgrade. Learn how KubernetesPodOperator and DockerOperator can fix this.
- [We're all using Airflow wrong and how to fix it](https://medium.com/bluecore-engineering/were-all-using-airflow-wrong-and-how-to-fix-it-a56f14cb0753) - [Jessica Laughlin](https://www.jldlaughlin.com/) shares three engineering problems associated with the Airflow design and how to solve them.
- [Getting started with Data Lineage](https://medium.com/dailymotion/getting-started-with-data-lineage-6307b2b429b3) - [Germain Tanguy](https://www.linkedin.com/in/germain-tanguy/) of [Dailymotion](https://www.dailymotion.com/) shares a data lineage prototype integrated to Apache Airflow.
- [Airflow: Lesser Known Tips, Tricks, and Best Practices](https://medium.com/datareply/airflow-lesser-known-tips-tricks-and-best-practises-cf4d4a90f8f) - [Kaxil Naik](https://www.linkedin.com/in/kaxil/) has explained the lesser-known yet very useful tips and best practices on using Airflow.
- [Testing in Airflow Part 1](https://medium.com/@chandukavar/testing-in-airflow-part-1-DAG-validation-tests-DAG-definition-tests-and-unit-tests-2aa94970570c) - [Chandu Kavar](https://twitter.com/chandukavar) has explained different categories of tests in Airflow. It includes DAG Validation Tests, DAG Definition Tests, and unit tests.
- [Testing in Airflow Part 2](https://medium.com/@chandukavar/testing-in-airflow-part-2-integration-tests-and-end-to-end-pipeline-tests-af0555cd1a82) - [Chandu Kavar](https://twitter.com/chandukavar) and [Sarang Shinde](https://www.linkedin.com/in/sarang-shinde-219a4873/) have explained Integration Tests and End-to-End Pipeline Tests.
- [Lessons learnt while Airflow-ing](https://medium.com/@nehiljain/lessons-learnt-while-airflow-ing-32d3b7fc3fbf) and [Airflow Part 2: Lessons learned](https://medium.com/snaptravel/airflow-part-2-lessons-learned-793fa3c0841e) - [Nehil Jain](https://twitter.com/nehiljain) has written a two-part series that covers the value of workflow schedulers, some best practices and pitfalls he found while working with Airflow.  The [second article](https://medium.com/snaptravel/airflow-part-2-lessons-learned-793fa3c0841e) in particular includes many production tips.
- [Airflow: Why is nothing working? - TL;DR Airflow’s SubDAGOperator causes deadlocks](https://medium.com/bluecore-engineering/airflow-why-is-nothing-working-f705eb6b7b04) by [Jessica Laughlin](https://twitter.com/thepressofjess) - Deep dive into troubleshooting a troublesome Airflow DAG with good tips on how to diagnosis problems.
- [Airflow Lessons from the Data Engineering Front in Chicago](https://medium.com/stanton-ventures-insights/airflow-lessons-from-the-data-engineering-front-in-chicago-9489e6ad5c3d) - [Alison Stanton](https://twitter.com/alison985) provides a list of tips to avoid gotchas in Airflow jobs.
- [Data quality checkers](https://drivy.engineering/data-quality/) - [Antoine Augusti](https://twitter.com/AntoineAugusti) describes the framework [drivy](https://www.drivy.co.uk/) has built atop Airflow to test their datasets for completeness, consistency, timeliness, uniqueness, validity and accuracy.
- [The Zen of Python and Apache Airflow](https://blog.godatadriven.com/zen-of-python-and-apache-airflow) - Blog post about how the Zen of Python can be applied to Airflow code.
- [Breaking up the Airflow DAG mono-repo](https://tech.scribd.com/blog/2020/breaking-up-the-DAG-repo.html) - This post describes how to support managing Airflow DAGs from multiple git repos through S3.
- [Improving Performance of Apache Airflow Scheduler](https://medium.com/databand-ai/improving-performance-of-apache-airflow-scheduler-507f4cb6462a) - A story of an adventure that allowed [Databand](https://databand.ai/) to speed up DAG parsing time 10 times
- [How SSENSE is using Apache Airflow to do Data Lineage on AWS](https://medium.com/ssense-tech/principled-data-engineering-part-ii-data-governance-30297abb2446) - Exploring the fundamental themes of architecting and governing a data lake on AWS using Apache Airflow.

## Libraries, Hooks, Utilities

- [AirFly](https://github.com/ryanchao2012/airfly) - Auto generate Airflow's DAG.py on the fly.
- [Airflow plugins](https://github.com/airflow-plugins/) - Central collection of repositories of various plugins for Airflow, including MailChimp, Trello, sftp, GitHub, etc.
- [test_DAGs](https://gist.github.com/criccomini/2862667822af7fae8b55682faef029a7) - a more complete solution for DAG integrity tests ([first Circle of Data’s Inferno are the first](https://medium.com/@ingwbaa/datas-inferno-7-circles-of-data-testing-hell-with-airflow-cef4adff58d8).
- [DAG-factory](https://github.com/ajbosco/DAG-factory) - A library for dynamically generating Apache Airflow DAGs from YAML configuration files.
- [Pylint-Airflow](https://github.com/BasPH/pylint-airflow) - A Pylint plugin for static code analysis on Airflow code.
- [DAG checks](https://github.com/politools/DAG-checks) - The DAG-checks consist of checks that can help you in maintaining your Apache Airflow instance.
- [Airflow DVC plugin](https://github.com/covid-genomics/airflow-dvc) - Plugin for open-source version-control system for data science and Machine Learning pipelines - [DVC](https://dvc.org/).

## Cloud Composer resources

*This section contains articles that apply to [Cloud Composer](https://cloud.google.com/composer) — a service built by Google Cloud based on Apache Airflow. Tricks and solutions are described here that are intended for Cloud Composer, but may be applicable to vanilla Airflow.*

- [Enabling Autoscaling in Google Cloud Composer](https://medium.com/traveloka-engineering/enabling-autoscaling-in-google-cloud-composer-ac84d3ddd60) - Supercharge your Cloud Composer deployment while saving up some cost during idle periods.
- [Scale your Composer environment together with your business](https://cloud.google.com/blog/products/data-analytics/scale-your-composer-environment-together-your-business) - The Celery Executor architecture and ways to ensure high scheduler performance.
- [The Smarter Way of Scaling With Composer’s Airflow Scheduler on GKE](https://medium.com/swlh/the-smarter-way-of-scaling-with-composers-airflow-scheduler-on-gke-88619238c77b) - [Roy Berkowitz](https://www.linkedin.com/in/roy-berkowitz-19922aa9/) discusses more effective use of nodes in the Cloud Composer service.

## Sample projects

- [GitLab Data Team DAGs](https://gitlab.com/gitlab-data/analytics/-/tree/master/DAGs) - Several DAGs used to build analytics for the GitLab platform.
