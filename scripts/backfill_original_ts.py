#!/usr/bin/env python3
"""
Backfill script to add 'original_ts' field to existing DynamoDB records
This is needed for the admin dashboard to properly filter and display analytics
"""

import boto3
from boto3.dynamodb.conditions import Attr

# Configuration
TABLE_NAME = 'NCMWDashboardSessionlogs'
REGION = 'us-west-2'

def backfill_original_ts():
    """Add original_ts field to records that don't have it"""
    dynamodb = boto3.resource('dynamodb', region_name=REGION)
    table = dynamodb.Table(TABLE_NAME)

    print(f"Scanning table: {TABLE_NAME}")
    print("="*60)

    # Scan for items without original_ts field
    response = table.scan(
        FilterExpression=Attr('original_ts').not_exists()
    )

    items_to_update = response.get('Items', [])

    # Continue scanning if there are more items
    while 'LastEvaluatedKey' in response:
        response = table.scan(
            FilterExpression=Attr('original_ts').not_exists(),
            ExclusiveStartKey=response['LastEvaluatedKey']
        )
        items_to_update.extend(response.get('Items', []))

    print(f"Found {len(items_to_update)} items without 'original_ts' field")

    if len(items_to_update) == 0:
        print("✅ All items already have 'original_ts' field!")
        return

    # Update each item
    updated_count = 0
    failed_count = 0

    for item in items_to_update:
        session_id = item.get('session_id')
        timestamp = item.get('timestamp')

        if not session_id or not timestamp:
            print(f"⚠️  Skipping item with missing keys: {item}")
            failed_count += 1
            continue

        try:
            # Use the existing timestamp as original_ts
            table.update_item(
                Key={
                    'session_id': session_id,
                    'timestamp': timestamp
                },
                UpdateExpression='SET original_ts = :ts',
                ExpressionAttributeValues={
                    ':ts': timestamp
                }
            )
            updated_count += 1

            if updated_count % 10 == 0:
                print(f"Updated {updated_count}/{len(items_to_update)} items...")

        except Exception as e:
            print(f"❌ Failed to update item {session_id}/{timestamp}: {e}")
            failed_count += 1

    print("="*60)
    print(f"✅ Successfully updated: {updated_count} items")
    if failed_count > 0:
        print(f"❌ Failed to update: {failed_count} items")
    print("="*60)

if __name__ == "__main__":
    print("Starting backfill process...")
    backfill_original_ts()
    print("Backfill complete!")
