# Copyright  Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
# -- This file has been generated --

# pylint: disable=C,E

import anthem
from ...common import (
    deferred_import,
    deferred_compute_parents
)


@anthem.log
def load_res_partner(ctx):
    model = ctx.env['res.partner'].with_context(tracking_disable=True)
    deferred_import(
        ctx,
        model,
        'install/generated/dj_test/comp4/res.partner.csv',
        defer_parent_computation=True)


@anthem.log
def load_res_partner_compute_parent(ctx):
    """Compute parent_left, parent_right"""
    deferred_compute_parents(ctx, 'res.partner')


@anthem.log
def post(ctx):
    load_res_partner(ctx)
    load_res_partner_compute_parent(ctx)
