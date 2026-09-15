# Design Document

## Architecture

Agent Layer
    |
Tools Layer
    |
Utility Layer
    |
JSON Data Files

## Tools

1. search_courses
2. get_course_details
3. enroll_in_course
4. unenroll_from_course
5. get_my_enrollments
6. get_popular_courses

## Ranking

BM25 ranking using:

- Title (weight 4)
- Description (weight 2)
- Skills (weight 1)
- Tags (weight 1)

## Future AWS Migration

Current:
JSON storage

Future:
AWS Bedrock AgentCore
+
Amazon OpenSearch
+
DynamoDB