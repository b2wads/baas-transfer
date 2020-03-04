#!/usr/bin/env bash

project_name="saque"

docker build -t registry.pe.hmg.asgard.b2w.io/baas/${project_name} . \
&& docker push registry.pe.hmg.asgard.b2w.io/baas/${project_name}
