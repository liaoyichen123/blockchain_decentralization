-- Builder
select count(distinct (from_address))
from builder_proposer_tx
         join (select distinct (relay_data.block_number) from relay_data) rd
              on builder_proposer_tx.block_number = rd.block_number;
-- Proposer
select count(distinct (to_address))
from builder_proposer_tx
         join (select distinct (relay_data.block_number) from relay_data) rd
              on builder_proposer_tx.block_number = rd.block_number;
-- Relay
select count(distinct (relay_data.relay)) from relay_data;
