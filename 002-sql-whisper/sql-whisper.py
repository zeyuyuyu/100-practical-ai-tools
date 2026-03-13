#!/usr/bin/env python3
import sys, argparse, os, litellm

# Usage: python sql-whisper.py -s schema.sql -q "get the users who signed up last week"
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--schema', type=str, required=True, help="Path to schema.sql file")
    parser.add_argument('-q', '--query', type=str, required=True, help="Natural language query")
    args = parser.parse_args()

    with open(args.schema, 'r') as f:
        schema = f.read()

    model = os.getenv("MODEL", "gpt-4o-mini")
    
    prompt = f"Given this DB schema:\n{schema}\n\nWrite a strictly correct SQL query for this request: '{args.query}'. RETURN ONLY SQL CODE, no markdown ticks."
    
    try:
        res = litellm.completion(model=model, messages=[{"role": "user", "content": prompt}])
        sql = res.choices[0].message.content.strip().replace("```sql","").replace("```","").strip()
        print(sql)
    except Exception as e:
        print(f"-- Error: {str(e)}")

if __name__ == "__main__":
    main()
