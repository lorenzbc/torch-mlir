# Part of the LLVM Project, under the Apache License v2.0 with LLVM Exceptions.
# See https://llvm.org/LICENSE.txt for license information.
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Also available under a BSD-style license. See LICENSE.

import torch

from torch_mlir_e2e_test.torchscript.framework import TestUtils
from torch_mlir_e2e_test.torchscript.registry import register_test_case
from torch_mlir_e2e_test.torchscript.annotations import annotate_args, export

# ==============================================================================

class NeFloatModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args([
        None,
        ([], torch.float64, True),
        ([], torch.float64, True),
    ])
    def forward(self, lhs, rhs):
        return float(lhs) != float(rhs)


@register_test_case(module_factory=lambda: NeFloatModule())
def NeFloatModule_basic(module, tu: TestUtils):
    module.forward(torch.rand((), dtype=torch.float64), torch.rand((), dtype=torch.float64))

# ==============================================================================

class EqFloatModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args([
        None,
        ([], torch.float64, True),
        ([], torch.float64, True),
    ])
    def forward(self, lhs, rhs):
        return float(lhs) == float(rhs)


@register_test_case(module_factory=lambda: EqFloatModule())
def EqFloatModule_basic(module, tu: TestUtils):
    module.forward(torch.rand((), dtype=torch.float64), torch.rand((), dtype=torch.float64))

# ==============================================================================

class GtFloatModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @export
    @annotate_args([
        None,
        ([], torch.float64, True),
        ([], torch.float64, True),
    ])
    def forward(self, lhs, rhs):
        return float(lhs) > float(rhs)


@register_test_case(module_factory=lambda: GtFloatModule())
def GtFloatModule_basic(module, tu: TestUtils):
    module.forward(torch.rand((), dtype=torch.float64), torch.rand((), dtype=torch.float64))