from agent_os.policies.schema import (
    PolicyDocument, PolicyRule, PolicyCondition,
    PolicyAction, PolicyOperator, PolicyDefaults,
)

policy = PolicyDocument(
    name="agent-safety",
    version="1.0",
    description="Safety policy for the react agent",
    defaults=PolicyDefaults(action=PolicyAction.ALLOW),
    rules=[
        PolicyRule(
            name="block-dangerous-tools",
            condition=PolicyCondition(
                field="tool_name",
                operator=PolicyOperator.IN,
                value=["query_database"],
            ),
            action=PolicyAction.DENY,
            message="Tool is blocked by safety policy",
            priority=100,
        ),
    ],
)