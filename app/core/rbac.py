import casbin
import os

def get_enforcer():
    model_conf = os.path.join(os.path.dirname(__file__), "rbac_model.conf")
    policy_csv = os.path.join(os.path.dirname(__file__), "rbac_policy.csv")
    return casbin.Enforcer(model_conf, policy_csv)
